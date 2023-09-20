from django.forms import ModelForm
from .models import Migrations, Feeding


class MigrationsForm(ModelForm):
  class Meta:
    model = Migrations
    fields = '__all__'


class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
