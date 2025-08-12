from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from shop.views import HomeView, LoginView, RegisterView, LegalView, ContactView, logout_view

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
