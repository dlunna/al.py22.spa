from .models import Link

def SocialNetwork_context(request):
    sn_ctx = {} #se crea el diccionario
    links = Link.objects.all()
    for elemento in links:
        sn_ctx[elemento.key] = elemento.url
    return sn_ctx
