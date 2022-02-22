from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category, Post

# Create your views here.

def web (render):
    return HttpResponse('<p>Notas</p>')

def home (request):
    objj = Post.objects.all()
    return render(request, "blog/fifi.html", {'clave':objj})

def category (request, category_id):

    #opcion 1
    #objj = Category.objects.get(id=category_id)
    #return render(request, "blog/category.html", {'clave':objj})

    #opcion 2
    #objj = get_object_or_404(Category, id=category_id)
    #objeto=Post.objects.filter(categories=objj)
    #return render(request, "blog/category.html", {'dlave':objj},{'clave':objeto})

    #opcion 3
    objj = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'clave':objj})