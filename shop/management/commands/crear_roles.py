from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from shop.models import Order

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios y asigna permisos básicos para empleados y clientes.'

    def handle(self, *args, **kwargs):
        # Grupo Empleado
        empleados, created = Group.objects.get_or_create(name='Empleado')
        # Permiso para ver pedidos
        content_type = ContentType.objects.get_for_model(Order)
        permiso_ver_pedidos, _ = Permission.objects.get_or_create(
            codename='view_order',
            name='Puede ver pedidos',
            content_type=content_type
        )
        empleados.permissions.add(permiso_ver_pedidos)

        # Grupo Cliente (sin permisos especiales)
        clientes, created = Group.objects.get_or_create(name='Cliente')

        self.stdout.write(self.style.SUCCESS('Grupos y permisos creados correctamente.'))
