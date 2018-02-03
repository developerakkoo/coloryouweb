from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def color(request):
    return render(request,'color.css')

def documentation(request):
    return render(request,'documentation.html')


def guide(request):
    return render(request,'guide.html')
