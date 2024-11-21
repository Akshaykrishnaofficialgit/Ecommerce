from django.shortcuts import render,redirect
from shop.models import Products
from cart.models import  Cart,Payment_table,Order_details
from django.contrib.auth.models import User
from django.contrib.auth import login
import razorpay

def add_to_cart(request,i):
    needed_product=Products.objects.get(id=i)
    needed_user=request.user
    try:
        c=Cart.objects.get(user=needed_user,product=needed_product)
        c.quantity+=1
        needed_product.stock-=1
        needed_product.save()
        c.save()
    except:
        c=Cart.objects.create(product=needed_product,user=needed_user,quantity=1)
        needed_product.stock-=1
        needed_product.save()
        c.save()

    return redirect('cart:cartview')

def remove_item(request,i):
    u=request.user
    p=Products.objects.get(id=i)
    c=Cart.objects.get(user=u,product=p)
    if c.quantity>0:
        c.quantity-=1
        c.save()
        p.stock+=1
        p.save()
    else:
        c.delete()
        p.stock+=1
        p.save()
    return redirect('cart:cartview')

def trash(request,i):
    u = request.user
    p = Products.objects.get(id=i)
    c = Cart.objects.get(user=u, product=p)
    c.delete()
    p.stock += c.quantity
    p.save()
    return redirect('cart:cartview')

def cart_view(request):
    sub_total=0
    u=request.user
    unit=0
    c=Cart.objects.filter(user=u)
    for i in c:
        unit+=1
        sub_total+=i.quantity*i.product.price
    total=sub_total+(40*unit)
    shipping=40*unit
    context={'cart':c,'sub_total':sub_total,'total':total,'shipping':shipping}
    return render(request,'cart.html',context)


def checkout(request):
    if request.method=="POST":
        a=request.POST['ad']
        phh=request.POST['ph']
        pin = request.POST['pin']
        total = 0
        u = request.user
        c = Cart.objects.filter(user=u)
        for i in c:
            total+=i.product.price*i.quantity+(40)

        client=razorpay.Client(auth=())
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        amount=response_payment['amount']
        order_id=response_payment['id']
        status=response_payment['status']
        if status=='created':
            p=Payment_table.objects.create(name=u.username,amount=amount,order_id=order_id)
            p.save()
            for i in c:
                o=Order_details.objects.create(product=i.product,user=i.user,phone=phh,adrress=a,pin=pin,order_id=order_id,no_of_items=i.quantity)
                o.save()
            context={'payment':response_payment,'name':u.username,'email':u.email}
            return render(request,'payment.html',context)
    return render(request,'Checkout.html')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def payment_status(request,p):
    u=User.objects.get(username=p)
    login(request,u)
    response=request.POST
    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }
    client=razorpay.Client(auth=())
    try:
        status=client.utility.verify_payment_signature(param_dict)
        print(status)
        p=Payment_table.objects.get(order_id=response['razorpay_order_id'])
        p.razorpay_payment_id=response['razorpay_payment_id']
        p.payment=True
        p.save()

        o=Order_details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status="completed"
            i.save()

        c=Cart.objects.filter(user=u)
        c.delete()


    except:
        pass
    return render(request,'paymentstatus.html')

def your_orders(request):
    u=request.user
    o=Order_details.objects.filter(user=u,payment_status='completed')
    context={'orders':o}
    return render(request,'Your_orders.html',context)
