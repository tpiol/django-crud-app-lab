from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes', views.shoe_index, name='shoe-index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe-detail'),
]