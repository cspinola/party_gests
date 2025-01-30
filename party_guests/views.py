from django.shortcuts import render

def home(request):
    return render(request,'guests/home.html')

def guests(request):
    pass