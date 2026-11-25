from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)  #You create an expense on November 24,You update its amount on November 25,created_at remains November 24,updated_at changes to November 25.
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) # it means that if a user is deleted, all their associated expenses will also be deleted.
    def __str__(self): #It controls how an Expense object is represented as readable text.instead of displaying "Expense object (1)" it will display the title of the expense. This is useful for debugging and for displaying expenses in the Django admin interface.
        return self.title

    