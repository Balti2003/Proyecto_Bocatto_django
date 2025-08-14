from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.utils.decorators import method_decorator

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

        # Validar stock
        if cantidad > producto.stock:
            messages.error(request, f"No puedes agregar más de {producto.stock} unidades.")
            return redirect("product_detail", pk=producto.id)

        carrito = request.session.get("carrito", {})

        # Si el producto ya está en el carrito
        if str(producto.id) in carrito:
            nueva_cantidad = carrito[str(producto.id)]["cantidad"] + cantidad
            if nueva_cantidad > producto.stock:
                messages.error(request, f"No puedes tener más de {producto.stock} unidades de este producto.")
                return redirect("product_detail", pk=producto.id)
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
    
    
# Vista de logout   
@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Has cerrado sesion correctamente")
    return HttpResponseRedirect(reverse('home'))