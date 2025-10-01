from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Vistas generales
class HomeView(TemplateView):
    template_name = "../templates/general/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        context['productos'] = Product.objects.all()[:8]
        return context


class LoginView(FormView):
    template_name = "../templates/general/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=usuario, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Has iniciado sesion correctamente")
            return HttpResponseRedirect(reverse('home'))
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

        # pasar opciones de pago y entrega al template
        payment_choices = Order.PAYMENT_METHODS
        delivery_choices = Order.DELIVERY_TYPES

        return render(request, self.template_name, {
            "carrito": carrito,
            "total": total,
            "payment_methods": payment_choices,
            "delivery_types": delivery_choices,
        })

    def post(self, request, *args, **kwargs):
        carrito = request.session.get("carrito", {})
        if not carrito:
            messages.error(request, "No hay productos en el carrito para procesar el pedido.")
            return redirect("carrito")

        total = sum(item["precio"] * item["cantidad"] for item in carrito.values())

        # recoger selección de método de pago y tipo de entrega
        selected_payment = request.POST.get('payment_method')
        selected_delivery = request.POST.get('delivery_type')

        # Validar que los valores estén entre las opciones permitidas
        valid_payments = [p[0] for p in Order.PAYMENT_METHODS]
        valid_deliveries = [d[0] for d in Order.DELIVERY_TYPES]

        if selected_payment not in valid_payments:
            messages.error(request, "Método de pago inválido.")
            return redirect("checkout")

        if selected_delivery not in valid_deliveries:
            messages.error(request, "Tipo de entrega inválido.")
            return redirect("checkout")

        # Crear el pedido con método de pago y tipo de entrega
        order = Order.objects.create(
            usuario=request.user,
            fecha=timezone.now(),
            total=total,
            estado="pendiente",
            payment_method=selected_payment,
            delivery_type=selected_delivery,
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

        # Agregar subtotales por cada item
        for item in items:
            item.subtotal = item.cantidad * item.precio_unitario

        context["items"] = items
        context["total"] = order.total
        # indicar si el usuario puede actualizar el estado (empleado o staff)
        user = self.request.user
        context['can_change_status'] = user.is_authenticated and (user.groups.filter(name="Empleado").exists() or user.is_staff)
        return context

    def post(self, request, *args, **kwargs):
        # manejar actualización del estado desde el formulario del detalle
        self.object = self.get_object()
        user = request.user
        if not (user.is_authenticated and (user.groups.filter(name="Empleado").exists() or user.is_staff)):
            messages.error(request, "No tienes permiso para cambiar el estado del pedido.")
            return redirect('order_detail', pk=self.object.id)

        nuevo_estado = request.POST.get('estado')
        if nuevo_estado not in dict(Order.ESTADOS).keys():
            messages.error(request, "Estado inválido.")
            return redirect('order_detail', pk=self.object.id)

        self.object.estado = nuevo_estado
        self.object.save()
        messages.success(request, f"Estado del pedido #{self.object.id} actualizado a {self.object.get_estado_display()}.")
        return redirect('order_detail', pk=self.object.id)


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = "../templates/shop/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        # Solo mostrar pedidos del usuario logueado
        return Order.objects.filter(usuario=self.request.user).order_by("-fecha")


# Vista de logout   
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))


class EmployeeDashboardView(UserPassesTestMixin, ListView):
    model = Order
    template_name = "shop/employee_dashboard.html"
    context_object_name = "orders"

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.groups.filter(name="Empleado").exists() or user.is_staff)

    def get_queryset(self):
        # Filtrar por estado si se pasa ?estado=<valor>
        estado = self.request.GET.get('estado', 'all')
        qs = Order.objects.all()
        if estado in ['pendiente', 'enviado', 'cancelado']:
            qs = qs.filter(estado=estado)
        return qs.order_by("-fecha")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # estadísticas globales por estado
        context["total_pedidos"] = Order.objects.count()
        context["pedidos_enviados"] = Order.objects.filter(estado="enviado").count()
        context["pedidos_pendientes"] = Order.objects.filter(estado="pendiente").count()
        context["pedidos_cancelados"] = Order.objects.filter(estado="cancelado").count()

        # filtro activo
        context['current_filter'] = self.request.GET.get('estado', 'all')

        # calcular subtotales por item para cada pedido (para uso en la plantilla)
        orders = context.get('orders', [])
        for order in orders:
            for item in order.items.all():
                item.subtotal = float(item.cantidad) * float(item.precio_unitario)

        return context