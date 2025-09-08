from django.shortcuts import render

class Shoe:
    def __init__(self, type, name, description):
        self.type = type
        self.name = name
        self.description = description

shoes = [
    Shoe('Air Jordan IV', 'Cement Grey', 'The Air Jordan IV was MJs first signature model to take flight. Complete with never before seen “Wings” acting as lace locks and an unforgettable color scheme, the silhouette now returns in its truest form. Nodding to its 1989 debut, the new Air Jordan IV features iconic Nike Air branding on both the heel and outsole.'),
    Shoe('Air Jordan I', 'Dark Mocha', 'Jordan Brand continued their Black Toe design theme in 2020 and released the Jordan 1 High Dark Mocha. The upper of the Jordan 1 High Dark Mocha features a Sail leather base with black leather surrounding the toe box and Mocha suede on the heel and ankle. A black leather Swoosh, Jordan Wings logo on the ankle, and Nike Air branding on the tongue pays homage to branding that can be found on the original 1985 Jordan 1. A Sail midsole and black outsole complete this Black Toe design.')
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoe_index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes})