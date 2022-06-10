from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from Stores.models import Product

from .basket import Basket
from django.contrib import messages

def basket_summary(request):
    # print(request.session['basket'], request.user)
    basket = Basket(request)
    # print('yes')
    wish_produits = Product.objects.filter(users_wishlist=request.user)
    # print(wish_produits)
    context = {
        'basket': basket,
        'wish_produits': wish_produits
    }
    return render(request, 'summary.html', context)


def basket_add(request):
    # print("yes")
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        qty = request.POST.get('productqty')
        if qty == '':
            qty = 1
        product_qty = int(qty)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        messages.success(request, "product was added")
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        # print(response)
        messages.success(request, "product was deleted")
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': basketsubtotal})
        messages.success(request, "product was updated")
        return response


def WhatsappData(message):
    import time
    import webbrowser as web
    import pyautogui as pg
    from .models import WhatsappNumber
    
    phone = WhatsappNumber.objects.all()[0]
    
    phone = "+237"+phone
    web.open('https://web.whatsapp.com/send?phone='+phone+'&text='+message)
    time.sleep(30)
    pg.press('enter')


def sendData(request):
    if request.method == 'POST':
        # phone = request.POST['phone']
        message = request.POST['message']
        
        WhatsappData(message)
        messages.success(request, "Message has successfuly sent ...")
        
        return redirect('Basket:basket_summary')
    else:
        return render(request, "sendData.html")