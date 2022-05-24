from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def post_blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def post_singlepost(request, pk):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    
    my_post = {
        'post': post,
        'posts': posts,
    }
    return render(request, 'blog/singlepost.html', my_post)
