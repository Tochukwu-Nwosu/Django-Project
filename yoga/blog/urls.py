from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_blog, name='post_blog'),
    path('singlepost/<int:pk>/', views.post_singlepost, name='post_singlepost'),
]
