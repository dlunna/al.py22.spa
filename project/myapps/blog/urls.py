from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.home, name="blog_home"),
    path('category/<int:category_id>/', blog_views.category, name="blog_category"),
]
