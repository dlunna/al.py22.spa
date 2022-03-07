from django import template
from myapps.webpages.models import WebPage

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = WebPage.objects.all()
    return pages