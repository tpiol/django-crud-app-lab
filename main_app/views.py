from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
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
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', {'shoe': shoe, 'cleaning_form': cleaning_form})

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

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