from django.shortcuts import render

app_name = 'about'

# Create your views here.
def post_about(request):
    return render(request, 'about/about.html', {})