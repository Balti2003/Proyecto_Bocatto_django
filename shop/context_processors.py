def es_empleado(request):
    if request.user.is_authenticated:
        return {'es_empleado': request.user.groups.filter(name='Empleados').exists()}
    return {'es_empleado': False}