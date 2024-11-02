from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'index.html')


def not_built(request):
    return render(request,'not_built.html')

def menu(request):
    return render(request,'menu.html')