from django.urls import path
from . import views as pages_views

urlpatterns = [
    #path('', pages_views.pages, name="pages"),
    path('<int:page_id>/', pages_views.page, name="pages"),
    path('<int:page_id>/<slug:page_slug>/', pages_views.page, name="page"),
]
