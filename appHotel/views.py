from django.shortcuts import render,redirect
from .models import Habitacion,Cliente,ClienteContacto,CompraDetalle,Compra,Venta,Venta_detalle,Producto,Proveedor,Planilla,Usuario,AccesoUsuario,Modulo,Registro,Reservacion,Empleado

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def stats(request):
    return render(request, 'stats.html')

def consult(request):
    return render(request, 'consult.html')

#CRUD
def createData(request):
    return render(request, "acciones/create.html")

def readData(request):
    return render(request, "acciones/read.html")

def updateData(request):
    return render(request, "acciones/update.html")

def deleteData(request):
    return render(request, "acciones/delete.html")

def rooms(request):
    rooms = Habitacion.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})