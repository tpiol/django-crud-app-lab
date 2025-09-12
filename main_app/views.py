from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Shoe, Closet
from .forms import CleaningForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def shoe_index(request):
    shoes = Shoe.objects.filter(user=request.user)
    return render(request, 'shoes/index.html', {'shoes': shoes})

@login_required
def shoe_detail(request,shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    closets_shoe_doesnt_have = Closet.objects.exclude(id__in = shoe.closets.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', 
            {'shoe': shoe, 'cleaning_form': cleaning_form,
                'closets': closets_shoe_doesnt_have})

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['name', 'type', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['name', 'type', 'description']

class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/shoes/'

@login_required
def add_cleaning(request, shoe_id):
    form = CleaningForm(request.POST)

    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = shoe_id
        new_cleaning.save()

    return redirect('shoe-detail', shoe_id=shoe_id)

class ClosetCreate(LoginRequiredMixin, CreateView):
    model = Closet
    fields = '__all__'

class ClosetList(LoginRequiredMixin, ListView):
    model = Closet

class ClosetDetail(LoginRequiredMixin, DetailView):
    model = Closet 

class ClosetUpdate(LoginRequiredMixin, UpdateView):
    model = Closet
    fields = ['name', 'location']

class ClosetDelete(LoginRequiredMixin, DeleteView):
    model = Closet
    success_url = '/closet/'

@login_required
def associate_closet(request, shoe_id, closet_id):
    Shoe.objects.get(id=shoe_id).closets.add(closet_id)
    return redirect('shoe-detail', shoe_id=shoe_id)

@login_required
def remove_closet(request, shoe_id, closet_id):
    Shoe.objects.get(id=shoe_id).closets.remove(closet_id)
    return redirect('shoe-detail', shoe_id=shoe_id)

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
           
            login(request, user)
            return redirect('shoe-index')
        else:
            error_message = 'Invalid sign up - try again'
   
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
