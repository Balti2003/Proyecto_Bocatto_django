from django.conf import settings
import mercadopago
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Count, Sum
from shop.mixins import RoleRequiredMixin
from .forms import LoginForm, ProductForm, RegistrationForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.admin.views.decorators import staff_member_required

# Vistas generales

#Home para clientes
class HomeView(LoginRequiredMixin, RoleRequiredMixin, TemplateView):
    role = "Clientes"
    template_name = "../templates/general/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['productos'] = Product.objects.all()[:8]
        return context


#Home para empleados
class HomeViewEmpleados(LoginRequiredMixin, RoleRequiredMixin, ListView):
    role = "Empleados"
    model = Order
    template_name = "../templates/general/home_empleado.html"
    context_object_name = "orders"
    ordering = ["-fecha"]

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.GET.get("estado", "all")

        if estado != "all":
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # filtro actual
        estado = self.request.GET.get("estado", "all")
        if estado != "all":
            orders = Order.objects.filter(estado=estado)
        else:
            orders = Order.objects.all()
        context["current_filter"] = estado

        # contadores
        context["total_pedidos"] = Order.objects.count()
        context["pedidos_pendientes_pago"] = Order.objects.filter(estado="pendiente_pago").count()
        context["pedidos_pagados"] = Order.objects.filter(estado="pagado").count()
        context["pedidos_preparacion"] = Order.objects.filter(estado="en_preparacion").count()
        context["pedidos_listo"] = Order.objects.filter(estado="listo").count()
        context["pedidos_en_camino"] = Order.objects.filter(estado="en_camino").count()
        context["pedidos_enviados"] = Order.objects.filter(estado__in=["enviado", "en_camino"]).count()
        context["pedidos_cancelados"] = Order.objects.filter(estado="cancelado").count()
        
        return context
    

class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        # si no está autenticado
        if not request.user.is_authenticated:
            return redirect('login')
        # usuarios administradores
        if request.user.groups.filter(name__in=['Empleados']).exists():
            return redirect('home-empleado')
        # por defecto cliente
        return redirect('home')


class LoginView(FormView):
    template_name = "../templates/general/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home-redirect")

    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=usuario, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Has iniciado sesion correctamente")
            return HttpResponseRedirect(reverse('home-redirect'))
        else:
            messages.add_message(self.request, messages.ERROR, "Usuario o contraseña incorrectos")
            return super(LoginView, self).form_valid(form)


class RegisterView(CreateView):
    model = User
    template_name = "../templates/general/register.html"
    success_url = reverse_lazy("login")
    form_class = RegistrationForm
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_name = '../templates/general/legal.html'
  

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = '../templates/general/profile.html'


@method_decorator(login_required, name='dispatch')
class ContactView(TemplateView, FormView):
    template_name = '../templates/general/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']
        
        messages.add_message(self.request, messages.SUCCESS, "Mensaje enviado correctamente")
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(PasswordChangeView):
    template_name = '../templates/general/password_change.html'
    success_url = reverse_lazy('password_change_done')


@method_decorator(login_required, name='dispatch')
class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = '../templates/general/password_change_done.html'


# Vistas de productos
@method_decorator(login_required, name='dispatch')
class ProductsByCategoryView(ListView):
    model = Product
    template_name = '../templates/shop/products_by_category.html'
    context_object_name = 'productos'

    def get_queryset(self):
        self.categoria = get_object_or_404(Category, id=self.kwargs['categoria_id'])
        return Product.objects.filter(categoria=self.categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context


@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = '../templates/shop/products_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = Product.objects.all()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['categoria_seleccionada'] = self.request.GET.get('categoria')
        return context
    

@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = '../templates/shop/products_detail.html'
    context_object_name = 'producto'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        context['productos_relacionados'] = Product.objects.filter(
            categoria=producto.categoria
        ).exclude(id=producto.id)[:4]
        return context
    

class ProductCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    role = "Empleados"
    model = Product
    form_class = ProductForm
    template_name = "../templates/shop/product_form.html"
    success_url = reverse_lazy("home-empleado")


#Vistas de carrito
@method_decorator(login_required, name='dispatch')
class CartView(TemplateView):
    template_name = "../templates/shop/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carrito = self.request.session.get("carrito", {})

        total = 0
        for id, item in carrito.items():
            subtotal = item["precio"] * item["cantidad"]
            item["subtotal"] = subtotal
            total += subtotal

        context["carrito"] = carrito
        context["total"] = total
        return context


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def post(self, request, producto_id):
        producto = get_object_or_404(Product, id=producto_id)
        cantidad = int(request.POST.get("cantidad", 1))

        carrito = request.session.get("carrito", {})

        # Si el producto ya está en el carrito
        if str(producto.id) in carrito:
            nueva_cantidad = carrito[str(producto.id)]["cantidad"] + cantidad
            carrito[str(producto.id)]["cantidad"] = nueva_cantidad
        else:
            carrito[str(producto.id)] = {
                "nombre": producto.nombre,
                'categoria': producto.categoria.nombre,
                "precio": float(producto.precio),
                "cantidad": cantidad,
                "imagen": producto.imagen.url if producto.imagen else None
            }

        request.session["carrito"] = carrito
        messages.success(request, f"{cantidad} unidad(es) de {producto.nombre} agregadas al carrito.")
        return redirect("carrito")
    

@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, producto_id):
        carrito = request.session.get("carrito", {})
        if str(producto_id) in carrito:
            del carrito[str(producto_id)]
            request.session["carrito"] = carrito
            messages.success(request, "Producto eliminado del carrito.")
        return redirect("carrito")
    

@method_decorator(login_required, name='dispatch')
class CheckoutView(LoginRequiredMixin, View):
    template_name = "../templates/shop/checkout.html"

    def get(self, request, *args, **kwargs):
        carrito = request.session.get("carrito", {})
        if not carrito:
            messages.warning(request, "Tu carrito está vacío.")
            return redirect("carrito")

        total = 0
        for prod_id, item in carrito.items():
            item["subtotal"] = item["precio"] * item["cantidad"]
            total += item["subtotal"]

        return render(request, self.template_name, {
            "carrito": carrito,
            "total": total
        })

    def post(self, request, *args, **kwargs):
        carrito = request.session.get("carrito", {})
        if not carrito:
            messages.error(request, "No hay productos en el carrito para procesar el pedido.")
            return redirect("carrito")

        total = sum(item["precio"] * item["cantidad"] for item in carrito.values())

        # Capturar los valores seleccionados del checkout
        metodo_pago = request.POST.get("metodo_pago")
        metodo_entrega = request.POST.get("metodo_entrega")

        if not metodo_pago or not metodo_entrega:
            messages.error(request, "Debes seleccionar método de pago y de entrega.")
            return redirect("checkout")

        # Crear el pedido
        order = Order.objects.create(
            usuario=request.user,
            fecha=timezone.now(),
            total=total,
            metodo_pago=metodo_pago,
            metodo_entrega=metodo_entrega,
        )

        # Crear los items asociados al pedido
        for prod_id, item in carrito.items():
            producto = Product.objects.get(id=prod_id)

            OrderItem.objects.create(
                pedido=order,
                producto=producto,
                cantidad=item["cantidad"],
                precio_unitario=item["precio"]
            )

        # Vaciar carrito de la sesión
        request.session["carrito"] = {}

        messages.success(request, f"Tu pedido #{order.id} ha sido creado con éxito.")
        return redirect("order_detail", pk=order.id)


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = "../templates/shop/order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        items = order.items.all()

        # Pasamos la flag para mostrar el form solo a empleados
        context["items"] = items
        context["total"] = order.total
        context["can_change_status"] = self.request.user.groups.filter(name="Empleados").exists()
        return context

    def post(self, request, *args, **kwargs):
        order = self.get_object()

        # Solo empleados pueden cambiar el estado
        if not request.user.groups.filter(name="Empleados").exists():
            messages.error(request, "No tenés permisos para cambiar el estado del pedido.")
            return redirect("order_detail", pk=order.pk)

        # Capturar nuevo estado desde el formulario
        nuevo_estado = request.POST.get("estado")

        if nuevo_estado in dict(order.ESTADOS).keys():
            order.estado = nuevo_estado
            order.save()
            messages.success(request, f"El estado del pedido #{order.id} se actualizó a {order.get_estado_display()}.")
        else:
            messages.error(request, "Estado inválido.")

        return redirect("order_detail", pk=order.pk)


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = "../templates/shop/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        # Solo mostrar pedidos del usuario logueado
        return Order.objects.filter(usuario=self.request.user).order_by("-fecha")


class AdminReportsView(LoginRequiredMixin, RoleRequiredMixin, View):
    template_name = "../templates/general/admin_reports.html"
    role = "Empleados"

    def get(self, request):
        # Pedidos por dia
        pedidos_por_dia = (
            Order.objects.values("fecha__date")
            .annotate(total=Count("id"))
            .order_by("fecha__date")
        )

        labels_dias = [str(x["fecha__date"]) for x in pedidos_por_dia]
        datos_dias = [x["total"] for x in pedidos_por_dia]

        # Ingresos por mes
        ingresos_por_mes = (
            Order.objects.values("fecha__month")
            .annotate(ingresos=Sum("total"))
            .order_by("fecha__month")
        )

        labels_meses = [f"Mes {x['fecha__month']}" for x in ingresos_por_mes]
        datos_meses = [float(x["ingresos"] or 0) for x in ingresos_por_mes]

        #Estados de pedidos
        estados = (
            Order.objects.values("estado")
            .annotate(total=Count("id"))
            .order_by("estado")
        )

        labels_estados = [x["estado"] for x in estados]
        datos_estados = [x["total"] for x in estados]

        contexto = {
            "labels_dias": labels_dias,
            "datos_dias": datos_dias,
            "labels_meses": labels_meses,
            "datos_meses": datos_meses,
            "labels_estados": labels_estados,
            "datos_estados": datos_estados,
        }

        return render(request, self.template_name, contexto)


# Vista de logout   
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))


#Mercado pago
class MercadoPagoInitView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, usuario=request.user)

        if order.estado != "pendiente_pago":
            messages.info(request, "Este pedido ya fue pagado o no requiere pago.")
            return redirect("order_detail", pk=order.id)

        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

        preference_data = {
            "items": [
                {
                    "title": f"Pedido #{order.id}",
                    "quantity": 1,
                    "currency_id": "ARS",
                    "unit_price": float(order.total),
                }
            ],
            "payer": {
                "email": request.user.email
            },
            "back_urls": {
                #Mercado Pago NO acepta localhost, por lo que en produccion se cambia
                "success": "https://www.google.com",
                "failure": "https://www.google.com",
            },
            #"auto_return": "approved",
        }

        result = sdk.preference().create(preference_data)
        
        preference = result["response"]
        
        payment_url = preference["init_point"]

        return redirect(payment_url)


class PaymentSuccessView(TemplateView):
    template_name = "../templates/shop/payment_success.html"


class PaymentFailureView(TemplateView):
    template_name = "../templates/shop/payment_failure.html"
