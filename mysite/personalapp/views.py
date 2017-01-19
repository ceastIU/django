from django.shortcuts import render

def index(request):
    return render(request, 'personalapp/home.html')
# Create your views here.
