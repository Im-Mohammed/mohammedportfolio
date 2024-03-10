from django.shortcuts import render

# Create your views here.
def skills(req):
    return render(req,'edu/Skills.html')