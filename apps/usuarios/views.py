from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate


# def index(request):
#     return render(request, 'usuarios/index.html')


def     inserir_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuarios/inserir_usuario.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha, is_active=False, is_staff=True)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso.')

def login(request):
    if request.method == 'GET':
        # Standard approach: Render the login template for a GET request
        return render(request, 'usuarios/login.html')
    else:
        # Correction 1: Use .get() method correctly with parentheses
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # Django's authenticate() function verifies credentials
        user = authenticate(request, username=username, password=senha)

        if user is not None:  # Check if authentication was successful
            # Correction 2: Use Django's built-in login function to establish a session
            auth_login(request, user)
            # Correction 3: Redirect the user after successful login
            return redirect('index')
        else:
            # Handle invalid credentials
            return HttpResponse('Usuário ou senha inválido.')

