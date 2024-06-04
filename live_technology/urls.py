from django.contrib import admin
from django.urls import path,include
from . views import*

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('recuperacion/', recuperacion, name='recuperacion'),
    path('plantilla/', plantilla, name='plantilla'),
    path('registro/', registro, name='registro'),
    path('admin/', admin.site.urls),
    path('cursos_virtuales/', cursos_virtuales, name='cursos_virtuales'),
    path('mis_cursos/', mis_cursos, name='mis_cursos'),
    path('compra/curso/', compracurso, name='compracurso'),
    path('about/', about, name='about'),
    path('live/', include('live.urls')),
]