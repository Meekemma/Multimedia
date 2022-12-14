from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PhotoForm, CategoryForm

# Create your views here.

def gallery(request):
    category=request.GET.get('category')
    if category == None:    
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name__contains=category)    

    categories=Category.objects.all()
    context={'photos':photos,  'categories': categories }
    return render(request, 'photo/gallary.html', context)



def viewPhoto(request, pk):
    photo=Photo.objects.get(id=pk)


    context={'photo':photo}
    return render(request, 'photo/view.html', context) 


def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method =='POST':
        form=PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallary')       
    else:
        form=PhotoForm()
        
    context={'form':form, 'categories':categories}
    return render(request, 'photo/add.html', context)


def addCategory(request):
    category = Category.objects.all()
    form=CategoryForm

    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    context={'form':form, 'categoty':category}
    return render(request, 'photo/category.html', context)                    
