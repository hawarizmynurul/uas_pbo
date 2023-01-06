from django.contrib import admin

# Register your models here.
from .models import*

class Data(admin.ModelAdmin):
    list_display = ["nama_sekolah", "titik_koordinat", "keterangan"]
    search_fields = ["nama_sekolah", "titik_koordinat"]
    list_filter = ["nama_sekolah"]
    list_per_page = 4

class data(admin.ModelAdmin):
    list_display = ["NPSN", "nama", "jmlhmurid"]
    search_fields = ["nama", "jmlhmurid"]
    list_filter = ["nama"]
    list_per_page = 4

admin.site.register(Sekolah, Data)
admin.site.register(murid, data)