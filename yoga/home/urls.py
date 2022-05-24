from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.post_home, name='post_home'),
]
