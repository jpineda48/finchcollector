from django.contrib import admin

from .models import Finch, Migrations

admin.site.register(Finch)
# Register your models here.
admin.site.register(Migrations)
