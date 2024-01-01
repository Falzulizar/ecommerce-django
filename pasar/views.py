from django.shortcuts import render, get_object_or_404, redirect
from .models import Barang, CartItem
from django.contrib import messages

def home(request):
    search_barang = request.GET.get('search')
    if search_barang:
        daftar_barang = Barang.objects.filter(nama__icontains=search_barang)
    else:
        daftar_barang = Barang.objects.all()
    return render(request, 'home.html', {'searchBarang': search_barang, 'daftar_barang': daftar_barang})

def detail(request, barang_id):
    barang = get_object_or_404(Barang, pk=barang_id)
    stok = barang.stok
    return render(request, 'detail.html', {'barang': barang, 'stok': stok})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def add_to_cart(request, barang_id):
    barang_id = int(barang_id)
    barang = Barang.objects.get(pk=barang_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1)) # jumlah pesanan dari form
    if quantity < 1:
        quantity = 1 # minimal 1
    # cart_item jika sudah ada pesanan makanan tersebut
    # created jika belum ada pesanan makanan tersebut maka di simpan dan created = true
    cart_item, created = CartItem.objects.get_or_create(barang=barang)
    # If the item exists, update the quantity and item_total
    if not created:
        cart_item.quantity += quantity
        cart_item.item_total = cart_item.quantity * barang.harga
        cart_item.save()
    else:
        cart_item.quantity = quantity
        cart_item.item_total = quantity * barang.harga
        cart_item.save()
    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item_total for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, barang_id):
    barang_id = int(barang_id)
    barang = Barang.objects.get(pk=barang_id)
    try:
        cart_item = CartItem.objects.get(barang=barang)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Barang, CartItem

def checkout(request):
    if request.method == 'POST':
        # Mengambil data dari form
        nama_pemesan = request.POST.get('nama_pemesan')
        nomor_hp = request.POST.get('nomor_hp')
        alamat_pengiriman = request.POST.get('alamat_pengiriman')
        metode_pembayaran = request.POST.get('metode_pembayaran')
        catatan_tambahan = request.POST.get('catatan_tambahan')

        # Menyimpan data ke sesi untuk ditampilkan di halaman order_summary
        request.session['nama_pemesan'] = nama_pemesan
        request.session['nomor_hp'] = nomor_hp
        request.session['alamat_pengiriman'] = alamat_pengiriman
        request.session['metode_pembayaran'] = metode_pembayaran
        request.session['catatan_tambahan'] = catatan_tambahan

        # Cek stok barang sebelum checkout
        cart_items = CartItem.objects.all()
        for cart_item in cart_items:
            if cart_item.quantity > cart_item.barang.stok:
                messages.error(request, f"Stok barang {cart_item.barang.nama} tidak mencukupi untuk pesanan Anda.")
                return redirect('cart')  # Redirect kembali ke halaman keranjang jika stok tidak mencukupi

        return redirect('order_summary')

    return render(request, 'checkout.html')

def order_summary(request):
    # Mengambil data dari sesi
    nama_pemesan = request.session.get('nama_pemesan')
    nomor_hp = request.session.get('nomor_hp')
    alamat_pengiriman = request.session.get('alamat_pengiriman')
    metode_pembayaran = request.session.get('metode_pembayaran')
    catatan_tambahan = request.session.get('catatan_tambahan')

    # Ambil semua item dalam cart
    cart_items = CartItem.objects.all()

    # Logika lainnya sesuai kebutuhan

    context = {
        'nama_pemesan': nama_pemesan,
        'nomor_hp': nomor_hp,
        'cart_items': cart_items,
        'alamat_pengiriman': alamat_pengiriman,
        'metode_pembayaran': metode_pembayaran,
        'catatan_tambahan': catatan_tambahan,
    }

    return render(request, 'order_summary.html', context)