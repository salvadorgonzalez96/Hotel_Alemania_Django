from django.contrib import admin

from django.contrib import admin

from .models import Registro,Venta,Habitacion,Reservacion,Planilla,Empleado,Cliente,ClienteContacto,Modulo,AccesoUsuario,Usuario,Producto,Compra,CompraDetalle,Proveedor,Venta_detalle

admin.site.register(Registro)
admin.site.register(Venta)
admin.site.register(Habitacion)
admin.site.register(Reservacion)
admin.site.register(Planilla)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(ClienteContacto)
admin.site.register(Modulo)
admin.site.register(AccesoUsuario)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(CompraDetalle)
admin.site.register(Proveedor)
admin.site.register(Venta_detalle)
# Register your models here.
