from django.shortcuts import render
from .forms import Contact, ContactForm
# Create your views here.


def index(request):
    return render(request, 'CodeApp/index.html')

def gallery(request):
    # ROUTES TO GALLERY
    return render(request, 'CodeApp/gallery.html')

def aboutus(request):
    # ROUTES TO ABOUT US
    return render(request, 'CodeApp/aboutus.html')

def resources(request):
    # ROUTES TO RESOURCE
    return render(request, 'CodeApp/resources.html')

def contact(request):
    # FOR CONTACT FORM
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        # SAVES FORM
        if form.is_valid():
            form.save()

    # ROUTES TO GALLERY/SYNCS FORM INFO TO PAGE
    return render(request, 'CodeApp/contact.html', {"form": ContactForm})