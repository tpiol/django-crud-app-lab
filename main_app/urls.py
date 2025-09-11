from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoe_index, name='shoe-index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe-detail'),

    path('shoes/create/', views.ShoeCreate.as_view(), name='shoe-create'),

    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe-update'),

    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe-delete'),
    
    path('shoes/<int:shoe_id>/add-cleaning/', views.add_cleaning, 
    name='add-cleaning'),

    path('closet/create/', views.ClosetCreate.as_view(), name='closet-create'),

    path('closet/<int:pk>/', views.ClosetDetail.as_view(), name='closet-detail'),
    path('closet/', views.ClosetList.as_view(), name='closet-index'),   

    path('closet/<int:pk>/update/', views.ClosetUpdate.as_view(), name='closet-update'),
    path('closet/<int:pk>/delete/', views.ClosetDelete.as_view(), name='closet-delete'),
]