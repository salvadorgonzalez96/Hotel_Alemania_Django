import datetime
from django.db import models
from django.utils import timezone

class Registro(models.Model):
    registro_codigo = models.IntegerField(primary_key=True)
    habitacion_codigo = models.ForeignKey('Habitacion', on_delete=models.CASCADE)
    registro_nombre_cliente = models.TextField(max_length=45)
    registro_nombre_empresa = models.TextField(max_length=45)
    registro_rtn = models.TextField(max_length=45)
    registro_telefono = models.TextField(max_length=45)
    registro_id = models.TextField(max_length=45)
    registro_pais = models.TextField(max_length=45)
    registro_procedencia = models.TextField(max_length=45)
    registro_profesion = models.TextField(max_length=45)
    registro_numero_personas = models.TextField(max_length=45)
    registro_niños = models.TextField(max_length=45)
    registro_numero_noches = models.TextField(max_length=45)
    registro_dia_entrada = models.TextField(max_length=45)
    registro_dia_salida = models.TextField(max_length=45)
    registro_tarifa_por_noche = models.TextField(max_length=45)
    registro_total = models.TextField(max_length=45)
    registro_deposito = models.TextField(max_length=45)
    registro_saldo = models.TextField(max_length=45)
    registro_form_de_pago = models.TextField(max_length=45)
    venta_codigo = models.ManyToManyField('Venta', related_name='registros')
    habitaciones = models.ManyToManyField('Habitacion', related_name='registros')
    registro_auto_marca = models.TextField(max_length=45)
    registro_auto_color = models.TextField(max_length=45)
    registro_firma = models.TextField(max_length=45)

    def __str__(self):
        return f'Registro {self.registro_codigo} - {self.registro_nombre_cliente}'


class Venta(models.Model):
    venta_codigo = models.IntegerField(primary_key=True)
    cliente_codigo = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    venta_nombre_cliente = models.CharField(max_length=45)
    venta_fecha = models.DateTimeField()
    venta_rtn = models.IntegerField()
    venta_descuento = models.DecimalField(max_digits=9, decimal_places=2)
    venta_subtotal_exonerado = models.DecimalField(max_digits=9, decimal_places=2)
    venta_subtotal_exento = models.DecimalField(max_digits=9, decimal_places=2)
    venta_importe_gravado_18 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_importe_gravado_15 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_importe_gravado_4 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_isv_18 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_isv_15 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_isv_4 = models.DecimalField(max_digits=9, decimal_places=2)
    venta_total = models.DecimalField(max_digits=9, decimal_places=2)
    venta_estado = models.CharField(max_length=45)
    # venta_detalle = models.ManyToManyField('VentaDetalle')

    def __str__(self):
        return f'Venta {self.venta_codigo}'


class Habitacion(models.Model):
    habitacion_codigo = models.TextField(max_length=45, primary_key=True)
    habitacion_tipo = models.TextField(max_length=45)
    # habitacion_numero_personas = models.TextField(max_length=45)
    # habitacion_mantenimiento = models.TextField(max_length=45)
    # habitacion_limpieza = models.TextField(max_length=45)
    habitacion_estado = models.TextField(max_length=45)
    habitacion_descripcion = models.TextField(max_length=45)
    # registros = models.ManyToManyField('Registro', related_name='habitaciones')
    # reservaciones = models.ManyToManyField('Reservacion', related_name='habitaciones')
    class Meta:
        db_table = 'tbl_habitacion'

    def __str__(self):
        return self.habitacion_codigo + self.habitacion_tipo


class Reservacion(models.Model):
    reservacion_codigo = models.IntegerField(primary_key=True)
    reservacion_nombre_cliente = models.TextField(max_length=45)
    reservacion_cliente_id = models.IntegerField(20)
    habitaciones = models.ManyToManyField('Habitacion', related_name='reservaciones')
    reservacion_fecha = models.DateTimeField()
    reservacion_dias = models.IntegerField()
    reservacion_abono = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Reservacion {self.reservacion_codigo} - {self.reservacion_nombre_cliente}'


class Planilla(models.Model):
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    planilla_pago_dia = models.DecimalField(max_digits=9, decimal_places=2)
    planilla_horas_extras = models.DecimalField(max_digits=9, decimal_places=2)
    planilla_detalle = models.CharField(max_length=45)
    planilla_estado = models.CharField(max_length=45)

    def __str__(self):
        return self.empleado.codigo
    
class Empleado(models.Model):
    empleado_codigo = models.CharField(max_length=45)
    empleado_nombre = models.CharField(max_length=45)
    empleado_apellido = models.CharField(max_length=45)
    empleado_identidad = models.PositiveBigIntegerField()
    empleado_telefono = models.PositiveIntegerField()
    empleado_estado = models.CharField(max_length=45)
    # planillas = models.ManyToManyField('Planilla')

    def __str__(self):
        return f'{self.empleado_nombre} {self.empleado_apellido}'

class Cliente(models.Model):
    cliente_codigo = models.CharField(max_length=45,primary_key=True)
    cliente_id = models.IntegerField()
    cliente_nombre = models.CharField(max_length=45)
    cliente_ciudad = models.CharField(max_length=45)
    cliente_rtn = models.IntegerField()
    cliente_estado = models.CharField(max_length=45)
    # cliente_contacto = models.ManyToManyField('self', blank=True)
    # contactos = models.ManyToManyField('ClienteContacto', related_name='clientes')

    class Meta:
        db_table = 'tbl_cliente'

    def __str__(self):
        return self.cliente_nombre

class ClienteContacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cliente_contacto_telefono = models.IntegerField(primary_key=True)
    cliente_contacto_correo = models.CharField(max_length=45)

    
    def __str__(self):
        return str(self.cliente_contacto_telefono)
    

class Modulo(models.Model):
    modulo_codigo = models.CharField(max_length=45, primary_key=True)
    modulo_nombre = models.CharField(max_length=45)
    modulo_descripcion = models.CharField(max_length=200)
    # acceso_usuarios = models.ManyToManyField('AccesoUsuario', related_name='modulos')

    def __str__(self):
        return self.modulo_nombre
    

class AccesoUsuario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    acceso_estado = models.CharField(max_length=45)
    modulos = models.ManyToManyField(Modulo, related_name='accesos_usuarios')
    usuarios = models.ManyToManyField('Usuario', related_name='accesos_modulos')

    def __str__(self):
        return f"{self.usuario} - {self.modulo}"
    

class Usuario(models.Model):
    usuario_codigo = models.IntegerField(primary_key=True)
    usuario_nick = models.CharField(max_length=45)
    usuario_clave = models.CharField(max_length=45)
    usuario_estado = models.CharField(max_length=45)
    # accesos = models.ManyToManyField(AccesoUsuario, related_name='usuarios')

    def __str__(self):
        return f"{self.usuario_nick}"
    

class Producto(models.Model):
    producto_codigo = models.CharField(max_length=45, primary_key=True)
    producto_descripcion = models.CharField(max_length=45)
    producto_precio = models.DecimalField(max_digits=9, decimal_places=2)
    producto_stock = models.IntegerField()
    compras = models.ManyToManyField('Compra', related_name='productos')

    def __str__(self):
        return f"{self.producto_descripcion}"
    
class Compra(models.Model):
    compra_codigo = models.IntegerField(primary_key=True)
    compra_fecha = models.DateTimeField()
    producto = models.ManyToManyField(Producto)
    compra_rtn = models.IntegerField()
    compra_descuento = models.DecimalField(max_digits=9, decimal_places=2)
    compra_subtotal_exonerado = models.DecimalField(max_digits=9, decimal_places=2)
    compra_subtotal_exento = models.DecimalField(max_digits=9, decimal_places=2)
    compra_importe_gravado_18 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_importe_gravado_15 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_importe_gravado_4 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_isv_18 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_isv_15 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_isv_4 = models.DecimalField(max_digits=9, decimal_places=2)
    compra_total = models.DecimalField(max_digits=9, decimal_places=2)
    compra_estado = models.CharField(max_length=45)

class CompraDetalle(models.Model):
    compra_codigo = models.ForeignKey('Compra', on_delete=models.CASCADE)
    proveedores_codigo = models.ManyToManyField('Proveedor')
    compra_detalle_precio_unidad = models.DecimalField(max_digits=9, decimal_places=2)
    compra_detalle_cantidad = models.IntegerField()
    compra_detalle_descripcion = models.TextField()

    def __str__(self):
        return f"{self.compra_codigo} - {self.compra_detalle_descripcion}"
    
class Proveedor(models.Model):
    proveedores_codigo = models.CharField(max_length=45, primary_key=True)
    proveedores_nombre = models.CharField(max_length=45)
    proveedores_telefono = models.CharField(max_length=25)
    proveedores_correo = models.CharField(max_length=45)
    proveedores_direccion = models.CharField(max_length=70)
    compra_detalle = models.ManyToManyField('CompraDetalle', blank=True)

    def __str__(self):
        return self.proveedores_nombre
    
class Venta_detalle(models.Model):
    venta_codigo = models.ForeignKey('Venta', on_delete=models.CASCADE)
    venta_detalle_precioU = models.CharField(max_length=45)
    venta_detalle_cantidad = models.CharField(max_length=45)
    venta_detalle_descripcion = models.CharField(max_length=45)
    # ventas = models.ManyToManyField(Venta, related_name='detalles')