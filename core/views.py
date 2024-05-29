from django.shortcuts import render, redirect
from .models import Service, Project, Blog, Message
from .forms import MessageForm  # Подставьте свой путь к форме, если он отличается

# Create your views here.
def index(request):
    service = Service.objects.all()[:3]
    project = Project.objects.all()[:3]
    blog = Blog.objects.all()[:3]
    context = {
        'service':service,
        'project':project,
        'blog':blog,
    }
    return render(request, 'index.html', context)

def service(request):
    service = Service.objects.all()
    return render(request, 'services.html', {'service':service})

def about(request):
    return render(request, 'about.html')

def project(request):
    project = Project.objects.all()
    return render(request, 'project.html', {'project':project})

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog':blog})

def blog_single(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog-single.html', {'blog':blog})


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm()
    
    return render(request, 'contact.html', {'form': form})