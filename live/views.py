
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def cambio_admin(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = PasswordChangeForm(user)

    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada con éxito.')
            return redirect('gestor_user')
        else:
            errors = dict(form.errors.items())
            messages.error(request, 'Hubo un error al cambiar la contraseña.')
            return JsonResponse({'success': False, 'error_message': errors}, status=400)

    return render(request, './admin/cambio_admin.html', {'form': form, 'user': user})

@login_required
def gestion_user_process(request):
    users = User.objects.all()
    return render(request, './admin/gestion_user.html', {'users': users})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo_electronico = request.POST.get('correo_electronico')
        contraseña = request.POST.get('contrasena')
        tipo_de_usuario = request.POST.get('tipo_usuario')

        try:
            if User.objects.filter(email=correo_electronico).exists():
                raise IntegrityError('El correo electrónico ya está en uso.')

            is_staff = tipo_de_usuario  # 'True' o 'False'
            nuevo_usuario = User.objects.create_user(
                username=usuario,
                last_name=apellido,
                email=correo_electronico,
                password=contraseña,
                first_name=nombre,
                is_staff=is_staff,
            )

            messages.success(request, 'Usuario creado con éxito.')
            return redirect('gestor_user')

        except IntegrityError as e:
            messages.error(request, str(e))
            return render(request, './admin/creacion_user.html')

    else:
        return render(request, './admin/creacion_user.html')

@login_required
def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo_electronico = request.POST.get('correo')

        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo_electronico
        usuario.save()

        messages.success(request, 'Usuario modificado con éxito.')
        return redirect('gestor_user')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('gestor_user')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)