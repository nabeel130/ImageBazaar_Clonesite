from django.shortcuts import render
from .models import Category , Image

# Create your views here.

def show_about_page(request):
    name = 'Google'
    link = 'https://www.google.co.in/'

    context = {
        'name' : name,
        'link' : link
    }
    return render(request , 'about.html' , context)

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    context = {
        'cats' : cats,
        'images' : images
    }
    return render(request, 'home.html' , context)
    


def show_category_page(request , cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    context = {
        'cats' : cats,
        'images' : images
    }
    return render(request, 'home.html' , context)
    