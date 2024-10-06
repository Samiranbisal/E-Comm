from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def category(request,id):
    return render(request, 'app/category.html', locals())