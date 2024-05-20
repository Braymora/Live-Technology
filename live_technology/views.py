from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):            
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            request.session['user_authenticated'] = True  # Establecer la bandera en True
            return redirect('cursos_virtuales')
        
        # Si el usuario no es válido, agregar un mensaje de error
        messages.error(request, 'Usuario o contraseña incorrectos')
        return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    
    # Si la solicitud no es POST, simplemente renderiza el formulario de login
    return render(request, 'login.html')

def logout_view(request): 
    logout(request)
    return redirect('index')

@login_required
def recuperacion(request):            
    return render(request, 'recuperacion.html')

@login_required
def plantilla(request):            
    return render(request, 'plantilla.html')

@login_required
def registro(request):            
    return render(request, 'registro.html')

@login_required
def cursos_virtuales(request):
    return render(request, 'cursos.html')