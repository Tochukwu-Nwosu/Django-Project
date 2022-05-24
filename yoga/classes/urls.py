from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.post_classes, name='post_classes'),
]