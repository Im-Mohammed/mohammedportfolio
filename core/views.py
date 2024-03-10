from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'core/home.html')
def contact(req):
    return render(req,'core/Contact.html')