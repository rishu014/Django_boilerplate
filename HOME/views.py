from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about section")

def services(request):
    return HttpResponse("this is services section")

def contactUs(request):
    return HttpResponse("this is contact us section")