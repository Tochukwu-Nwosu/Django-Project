from django.shortcuts import render
from .forms import ContactForm

# from django.shortcuts import redirect

# Create your views here.

def post_contact(request):
    # if request.method == "POST":
    #     form = ContactForm(request.POST)
        
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
