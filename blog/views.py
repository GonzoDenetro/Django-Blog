from django.shortcuts import render, redirect, get_object_or_404
from .models import Post #Importamos nuestro modelo Post
from .forms import PostForm #Importamos nuestro formulario Post (Para crear un post)
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()} #Como estamos usando un Model Form vamos asociar el formulario con el modelo
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST) #Creamos una instancia de PostForm con la información que se lleno en el fomrulario
        #Validamos el usuario
        if form.is_valid(): 
            user = form.save(commit=False)
            user.autor = request.user
            user.save() #Guardamos la información en la base de datos
            messages.success(request, "Ypur post has been created succesfully")
            return redirect('posts') #Redireccionamos a la página de posts
        else:
            messages.error(request, "There was an error creating the post, check the fields")
            return render(request, 'blog/post_form.html', {'form': form})
        

@login_required
def edit_post(request, id):
    queryset = Post.objects.filter(autor=request.user) #Obtenemos los post del usuario
    post = get_object_or_404(queryset, id=id) #Traemos a nuestro objeto por medio de su id
    
    if request.method == "GET":
        context = {
                    "form": PostForm(instance=post), 
                    'id': id
                   } #Como contexto pasamos instancia el blogpos que tenmos creado
        return render(request, 'blog/post_form.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post) #Guardamos la nueva información en la instancia anterior
        
        if form.is_valid():
            form.save() #Guardamos en la base de datos
            messages.success(request, "Your post haas been updated succesfully")
            return redirect('posts')
        
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})


@login_required    
def delete_post(request, id):
    queryset = Post.objects.filter(autor=request.user) #Obtenemos los posts del usuario
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}
    
    if request.method == 'GET':
        return render(request, 'blog/delete_post.html', context)
    
    elif request.method == 'POST':
        post.delete() #Eliminamos nuestro modelo de la base de datos
        messages.success(request, "Your post has been deleted succesfully")
        return redirect ('posts')
    
    
def home(request):
    posts = Post.objects.all() #Traemos todo el contenido que esta en nuestro modelo, para usarlo en el templates
    context = {
        'posts': posts,
        'title': 'Zen de Python'
    }
    return render(request, 'blog/home.html', context)


def about(request): 
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'GET':
        context = {'form': ContactForm()}
        return render(request, 'blog/contact.html', context)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Manage data
            pass