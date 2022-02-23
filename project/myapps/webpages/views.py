from django.shortcuts import render, get_object_or_404
from .models import WebPage

# Create your views here.

# Se recuperan todas la páginas en un objeto
def pages(request):
    pages = get_object_or_404(WebPage)
    return render(request, 'webpages/avisos.html', {'pages':pages})


def page(request, page_id):
    page = get_object_or_404(WebPage, id=page_id )
    return render(request, 'webpages/aviso.html', {'page':page})

#solo se recupera 1 de acuerdo al ID
#def page(request, page_id, page_slug):
#    page = get_object_or_404(WebPage, id=page_id )
#    return render(request, 'pages/aviso.html', {'page':page})
