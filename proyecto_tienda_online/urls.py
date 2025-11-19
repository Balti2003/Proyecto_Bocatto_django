from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from shop.views import HomeRedirectView, HomeView, HomeViewEmpleados, LoginView, RegisterView, LegalView, ContactView, ProfileView, AdminReportsView, logout_view

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home-redirect"),
    path("cliente/", HomeView.as_view(), name="home"),
    path("empleado/", HomeViewEmpleados.as_view(), name="home-empleado"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("reportes/", AdminReportsView.as_view(), name="admin_reports"),
    
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
