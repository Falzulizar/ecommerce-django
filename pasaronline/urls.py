"""
URL configuration for pasaronline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pasar import views as pasarView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pasarView.home, name='home'),
    path('detail/<int:barang_id>/', pasarView.detail, name='detail'),
    path('cart/', pasarView.view_cart, name='cart'),
    path('add_to_cart/<int:barang_id>/', pasarView.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:barang_id>/', pasarView.remove_from_cart, name='remove_from_cart'),
    path('checkout/', pasarView.checkout, name='checkout'),
    path('order_summary/', pasarView.order_summary, name='order_summary'),
    path('contact/', pasarView.contact, name='contact'),
    path('about/', pasarView.about, name='about')
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)