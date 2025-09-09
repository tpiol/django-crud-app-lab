from django.db import models

class Shoe(models.Model): 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name