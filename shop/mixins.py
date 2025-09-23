from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class RoleRequiredMixin(UserPassesTestMixin):
    role = "Clientes"

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if self.role is None:
            return False
        return user.groups.filter(name=self.role).exists()

    def handle_no_permission(self):
        # Podés personalizar: redirigir a login o tirar 403
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        raise PermissionDenied("No tenés permiso para ver esta página.")
