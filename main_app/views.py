from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Closet
from .forms import CleaningForm

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
    closets_shoe_doesnt_have = Closet.objects.exclude(id__in = shoe.closets.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', 
            {'shoe': shoe, 'cleaning_form': cleaning_form,
                'closets': closets_shoe_doesnt_have})

class ShoeCreate(CreateView):
    model = Shoe
    fields = ['name', 'type', 'description']

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['name', 'type', 'description']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

def add_cleaning(request, shoe_id):
    form = CleaningForm(request.POST)

    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = shoe_id
        new_cleaning.save()

    return redirect('shoe-detail', shoe_id=shoe_id)

class ClosetCreate(CreateView):
    model = Closet
    fields = '__all__'

class ClosetList(ListView):
    model = Closet

class ClosetDetail(DetailView):
    model = Closet 

class ClosetUpdate(UpdateView):
    model = Closet
    fields = ['name', 'location']

class ClosetDelete(DeleteView):
    model = Closet
    success_url = '/closet/'

def associate_closet(request, shoe_id, closet_id):
    Shoe.objects.get(id=shoe_id).closets.add(closet_id)
    return redirect('shoe-detail', shoe_id=shoe_id)

def remove_closet(request, shoe_id, closet_id):
    Shoe.objects.get(id=shoe_id).closets.remove(closet_id)
    return redirect('shoe-detail', shoe_id=shoe_id)
