from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Una pizza de toda la vida"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Topping(models.Model):
    """Topping de la pizza"""
    name = models.CharField(max_length=50)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    

    

