from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        Item.objects.create(name=name, email=email, location=location)
        return redirect('index')
    return render(request, 'add.html')

def edit(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.email = request.POST.get('email')
        item.location = request.POST.get('location')
        item.save()
        return redirect('index')
    return render(request, 'edit.html', {'item': item})

def delete(request, id):
    Item.objects.get(id=id).delete()
    return redirect('index')
