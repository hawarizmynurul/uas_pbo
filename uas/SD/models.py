from django.db import models

# Create your models here.
class Sekolah(models.Model):
    nama_sekolah = models.CharField(max_length=50)
    titik_koordinat = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama_sekolah

class murid(models.Model):
    NPSN = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    jmlhmurid = models.CharField(max_length=50)

    def __str__(self):
        return self.NPSN