from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def company(request):
    return render(request, 'main/company.html')

def rast(request):
    return render(request, 'main/rast.html')

def poly(request):
    return render(request, 'main/poly.html')


