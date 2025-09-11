from django.db import models
from django.urls import reverse

CLEANING_METHODS = [
        ('HAND', 'Hand Wash (Soap & Water)'),
        ('WIPES', 'Sneaker Wipes / Magic Eraser'),
        ('MACHINE', 'Machine Wash'),
        ('DRY', 'Dry Brush'),
        ('KIT', 'Sneaker Cleaning Kit'),
        ('STEAM', 'Steam Cleaning'),
        ('SOLE', 'Sole Whitening'),
        ('SUEDE', 'Suede/Nubuck Care'),
        ('LEATHER', 'Leather Care'),
        ('PRO', 'Professional Service'),
    ]

class Closet(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('closet-detail', kwargs={'pk': self.id})

class Shoe(models.Model): 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    closets = models.ManyToManyField(Closet)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shoe-detail", kwargs={"shoe_id": self.id})
    
class Cleaning(models.Model):
    date = models.DateField('Date Cleaned')
    cleaning_methods = models.CharField(
        max_length=7,
        choices=CLEANING_METHODS,
        default=CLEANING_METHODS[0][0]
    )
 
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_cleaning_methods_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']  

