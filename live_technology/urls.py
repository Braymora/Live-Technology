from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperacion/', views.recuperacion, name='recuperacion'),
    path('plantilla/', views.plantilla, name='plantilla'),
    path('registro/', views.registro, name='registro'),
    path('admin/', admin.site.urls),
    path('cursos_virtuales/', views.cursos_virtuales, name='cursos_virtuales'),
    path('mis_cursos/', views.mis_cursos, name='mis_cursos')
]
