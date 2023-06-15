from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('stats', views.stats, name='stats'),
    path('consult', views.consult, name='consult'),
    path('create', views.createData, name='create'),
    path('update', views.updateData, name='update'),
    path('delete', views.deleteData, name='delete'),
    path('read', views.readData, name='read'),
    path('rooms', views.rooms, name='rooms'),
]