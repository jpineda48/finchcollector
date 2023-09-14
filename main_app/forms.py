from django.forms import ModelForm
from .models import Migrations


class MigrationsForm(ModelForm):
  class Meta:
    model = Migrations
    fields = '__all__'