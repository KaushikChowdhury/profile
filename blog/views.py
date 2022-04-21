from django.shortcuts import render

# Create your views here.
def blog(request):

    return render(request, 'blog/blog.html')

def contact(request):

    return render(request, 'blog/contact.html')

def index(request):

    return render(request, 'blog/index.html')

def projects(request):

    return render(request, 'blog/projects.html')

