from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoe_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})

def shoe_detail(request,shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/detail.html', {'shoe': shoe})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['name', 'type', 'description']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'