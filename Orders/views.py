from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from Basket.basket import Basket

from .models import Order, OrderItem, PayementMethode
from .forms import PayementForm

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse


def checkout(request):
    basket = Basket(request)
    if request.method == 'POST':
        print('yes')
    else:
        form = PayementForm()
        context = {
            'form': form,
            'prixTotal': basket.get_total_price()
        }
        return render(request, 'payement_methode.html', context)

def add(request):
    basket = Basket(request)
    # if request.POST.get('action') == 'post':
    if request.method == 'POST':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country_code = request.POST.get('country_code')
        payment_option_id = request.POST.get('payment_option')
        payment_option = PayementMethode.objects.get(id=payment_option_id)
        # print(payment_option)

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                        user_id=user_id, address=address, city=city, postal_code=postal_code,
                        country_code=country_code, total_paid=baskettotal, order_key=order_key,
                        payment_option=payment_option
                    )
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        # return response
        return redirect('Stores:store_home')

    else:
        form = PayementForm()
        context = {
            'form': form,
            'prixTotal': basket.get_total_price(),
        }
        return render(request, 'payement_methode.html', context)



@csrf_exempt
def payementSelect(request):
    data = request.body.decode('UTF-8')
    
    id = int(data.split()[4])
    
    payement_method = PayementMethode.objects.get(pk=id)

    try:
        result = payement_method.image.url
    except:
        number = payement_method.number_id
        name_of_the_beneficiary = payement_method.name_of_the_beneficiary
        result = (number, name_of_the_beneficiary)

    return JsonResponse({"payement_method_info": result})


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders