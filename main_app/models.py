from django.db import models

from django.urls import reverse



# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    diet = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})


class Migrations(models.Model):
    destination = models.CharField()
    departuredate = models.DateField()
    stops = models.TextField('stops along the way',max_length=250)

    

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.destination} on {self.departuredate}"