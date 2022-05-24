from django.urls import path
from . import views

app_name = 'instructors'

urlpatterns = [
    path('', views.post_instructors, name='post_instructors'),
]