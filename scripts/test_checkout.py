import os
import sys
PROJECT_ROOT = '/home/elias/CODE/Proyecto_Bocatto_django'
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_tienda_online.settings')
django.setup()

from django.contrib.auth import get_user_model
from shop.models import Order, Product, Category

c = Client()
User = get_user_model()

username = 'test_checkout_user'
password = 'testpass123'
user, created = User.objects.get_or_create(username=username)
if created:
    user.set_password(password)
    user.save()

# login via client
logged_in = c.login(username=username, password=password)
print('logged_in ->', logged_in)

# ensure product exists
product = Product.objects.first()
if not product:
    cat, _ = Category.objects.get_or_create(nombre='Test')
    product = Product.objects.create(nombre='ProdTest', descripcion='x', precio=100.0, categoria=cat)

# set session cart
session = c.session
session['carrito'] = {str(product.id): {'nombre': product.nombre, 'precio': float(product.precio), 'cantidad': 2, 'subtotal': float(product.precio)*2}}
session.save()

# perform POST to checkout (URL as defined in shop/urls.py)
resp = c.post('/cart/checkout/', {'payment_method': 'mercadopago', 'delivery_type': 'delivery'}, follow=True)
print('POST status:', resp.status_code)

# fetch last order
order = Order.objects.filter(usuario=user).order_by('-id').first()
if order:
    print('Order created:', order.id, 'payment:', order.payment_method, 'delivery:', order.delivery_type)
else:
    print('No order found for user')
