from django.contrib import admin

# Register your models here.
from .models import Director, Peliculas

admin.site.register(Director)
admin.site.register(Peliculas)
