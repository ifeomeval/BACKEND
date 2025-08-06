from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, name='user')
    number_of_people = models.PositiveIntegerField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, name='menu')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu.name} at {self.date}"

