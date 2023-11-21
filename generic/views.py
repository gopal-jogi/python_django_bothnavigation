from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def salman(request):
    return render(request,'salman.html')