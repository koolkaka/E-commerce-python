from shop.models import Category, Customer, ShopCart
from django.shortcuts import render

def about(request):
    current_user = request.user

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    
    catgories = Category.objects.all()
    carts = ShopCart.objects.filter(user_id=current_user.id)
    
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    details = {
        'qty':qty,
        'total':total,
        'carts':carts,
        'categories':catgories,
        'customer':customer
    }
    return render(request, 'about.html', details)