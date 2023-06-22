from django.contrib import admin
from .models import Marca, Talla, Producto

# Register your models here.

admin.site.register(Marca)
admin.site.register(Talla)
admin.site.register(Producto)
