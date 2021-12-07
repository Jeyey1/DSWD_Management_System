from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Product, Supplier, Buyer, Season

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_season = Season.objects.count()
    
    context = {
        'Pwd': total_product,
        'Youth': total_supplier,
        'women': total_buyer,
        'elder': total_season,
        
    }
    return render(request, 'dashboard.html', context)