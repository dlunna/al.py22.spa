from django.shortcuts import render, HttpResponse
from .models import Category, Post

# Create your views here.

def web (render):
    return HttpResponse('<p>Notas</p>')

def home (request):
    objj = Post.objects.all()
    return render(request, "blog/fifi.html", {'clave':objj})