from django.shortcuts import render, HttpResponse

# Create your views here.

def web(request):
    return HttpResponse("<p>LovelySPA</p>")

def root(request):
    return render(request, "core/root.html")

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")
