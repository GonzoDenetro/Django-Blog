from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_in(request):
    
    if request.method == 'GET':
        if request.user.is_authenticated: #Checamos si tenemos una sesión creada
            return redirect('posts')
        
        form = LoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) #Autenticamos que exista el usuario
            print('*'*100)
            print(user)
            
            if user:
                login(request, user) #Registramos al usuario en la sesión actual 
                messages.success(request,f'Hi {user.username.title()}, welcome back!')
                return redirect('posts')
        
         # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})


def sign_out(request):
    logout(request) #Cierra la sesión del usuario, borra la información de la sesión relacionada con el usuario
    messages.success(request, "You have been logged out")
    return redirect('login')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST) #Creamos una instancia con la información llenada
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save() #Guardamos en la Base de Datos
            messages.success(request, "You have Register Succesfully")
            login(request, user)
            return redirect('posts')
        
        else:
            return render(request, 'users/register.html', {'form': form})