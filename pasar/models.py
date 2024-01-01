from django.db import models
from django.core.validators import RegexValidator

class Toko(models.Model):
    nama = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="min 8 digit")
    telpon = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    alamat = models.TextField()

    def __str__(self) -> str:
        return self.nama

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True,null=True)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='movie/images/')
    stok = models.IntegerField()
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    TERSEDIA = (
        ('1', 'Tersedia'),
        ('0', 'Tidak tersedia')
    )
    tersedia = models.CharField(max_length=1, choices=TERSEDIA)

    def __str__(self) -> str:
        return self.nama
    
class CartItem(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2,
    blank=True, null=True)