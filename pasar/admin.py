from django.contrib import admin
from .models import Barang
from .models import Toko

# Register your models here.
admin.site.register(Barang)
admin.site.register(Toko)