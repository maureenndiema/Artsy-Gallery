from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image,Location,Category

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
