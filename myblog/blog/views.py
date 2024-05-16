from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def starting_page(request):
    # pass
    return render(request, 'blog/index.html')
    

def posts(request):
    # pass
    return render(request, 'blog/posts.html')

def single_post(request):
    pass