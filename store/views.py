from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
def store(request) :
    if request.user.is_authenticated :
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        cartItems = order.get_cart_item
       
    else :
        items=[]
        order ={'get_cart_items': 0 , 'get_cart_total':0}
        cartItems=order['get_cart_items']


    products =Product.objects.all()
    context ={"products": products,'cartItems':cartItems}



    return render(request, 'store/store.html',context)


def cart(request) :
    if request.user.is_authenticated :
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_item_set.all()
        cartItems=order.get_cart_item
    else :
        items=[]
        order ={'get_cart_items': 0 , 'get_cart_total':0}

        cartItems=order['get_cart_items']
    
    context ={'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store/cart.html',context)


def checkout(request) :
    
    if request.user.is_authenticated :
        
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.order_item_set.all()
        cartItems=order.get_cart_item

       
    else :
        items=[]
        order ={'get_cart_items': 0 , 'get_cart_total':0}
        cartItems=order['get_cart_items']
    

    context ={'items':items,'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html',context)


def updateItem(request):
    data= json.loads(request.body)
    productId =data['productId']
    action =data['action']
    print('productId',productId)
    print('action',action)

    customer = request.user.customer
    product =Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = Order_Item.objects.get_or_create(order=order,product=product)


    if action == 'add':
        orderItem.quantity=(orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity -1)

    orderItem.save()
    if orderItem.quantity <=0 :
        orderItem.delete()

    return JsonResponse("item was added",safe=False)




def processOrder(request):
        return JsonResponse("payment submitted.. ",safe=False)



def viewProduct(request):
    data= json.loads(request.body)
    productId =data['productId']
    action =data['action']
    print('productId',productId)
    print('action',action)

    customer = request.user.customer
    product =Product.objects.get(id=productId)

    return JsonResponse("product",safe=False)
    

