from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts, name='post_all'),
    path('detail/<int:pk>/', views.getPost, name='post_detail'),
]
