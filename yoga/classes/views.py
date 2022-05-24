from django.shortcuts import render
from .models import Post

# Create your views here.
def post_classes(request):
    posts = Post.objects.all()
    return render(request, 'classes/classes.html', {'posts': posts})
