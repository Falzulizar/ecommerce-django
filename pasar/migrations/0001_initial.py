# Generated by Django 4.2.7 on 2023-11-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('telpon', models.CharField(max_length=15)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
                ('harga', models.IntegerField()),
                ('gambar', models.URLField()),
                ('stok', models.IntegerField()),
                ('toko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasar.toko')),
            ],
        ),
    ]