from django.shortcuts import render

# Create your views here.
def post_home(request):
    return render(request, 'home/index.html', {})
