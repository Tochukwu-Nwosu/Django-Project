from django.shortcuts import render
from . models import Image_row1, Image_row2

# Create your views here.

def post_instructors(request):
    row1 = Image_row1.objects.all()
    row2 = Image_row2.objects.all()
    
    container = {
        'row1': row1, 
        'row2': row2,
        }
    return render(request, 'instructors/instructors.html', container)