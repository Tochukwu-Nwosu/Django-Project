from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.post_contact, name='post_contact'),
]
