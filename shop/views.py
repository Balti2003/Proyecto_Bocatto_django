from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from shop.mixins import RoleRequiredMixin
from .forms import LoginForm, ProductForm, RegistrationForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

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
        context["current_filter"] = estado

        # contadores
        context["total_pedidos"] = Order.objects.count()
        context["pedidos_pendientes"] = Order.objects.filter(estado="pendiente").count()
        context["pedidos_enviados"] = Order.objects.filter(estado="enviado").count()
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
        metodo_pago = request.POST.get("metodo_pago", "efectivo")
        metodo_entrega = request.POST.get("metodo_entrega", "retiro")

        # Crear el pedido
        order = Order.objects.create(
            usuario=request.user,
            fecha=timezone.now(),
            total=total,
            estado="pendiente",
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


# Vista de logout   
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))