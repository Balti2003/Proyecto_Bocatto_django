from django import forms
from django.contrib.auth.models import User
from shop.models import Category, Product

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "password",
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
    
        return user


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}),
        label="Nombre"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
        label="Correo electrónico"
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_mensaje', 'rows': 5}),
        label="Mensaje"
    )


class ProductForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}),
        label="Nombre"
    )

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_descripcion', 'rows': 3}),
        label="Descripción"
    )

    precio = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_precio'}),
        label="Precio"
    )

    categoria = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_categoria'}),
        label="Categoría"
    )

    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'id_imagen'}),
        label="Imagen"
    )

    class Meta:
        model = Product
        fields = ["nombre", "descripcion", "precio", "categoria", "imagen"]