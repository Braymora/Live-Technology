
from django.urls import path
from . views import*

urlpatterns = [
    path('cambio/contraseña/admin/<int:user_id>/', cambio_admin, name='cambio_admin'),
    path('gestion/user/admin/', gestion_user_process, name='gestor_user'),
    path('tarificador/Gestion/crea/Usuario/', crear_usuario, name='crear_usuario'),
    path('tarificador/eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),  
    path('tarificador/modificar_usuario/<int:usuario_id>/', modificar_usuario, name='modificar_usuario'),
    ]