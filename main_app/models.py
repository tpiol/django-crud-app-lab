from django.db import models
from django.urls import reverse

class Shoe(models.Model): 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shoe-detail", kwargs={"shoe_id": self.id})
    