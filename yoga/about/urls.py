from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.post_about, name='post_about'),
]