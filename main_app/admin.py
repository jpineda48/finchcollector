from django.contrib import admin

from .models import Finch, Migrations, Feeding, Toy

admin.site.register(Finch)
# Register your models here.
admin.site.register(Migrations)

admin.site.register(Feeding)
admin.site.register(Toy)
