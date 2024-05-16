from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperacion/', views.recuperacion, name='recuperacion'),
    path('registro/', views.registro, name='registro'),
    path('admin/', admin.site.urls),
]
