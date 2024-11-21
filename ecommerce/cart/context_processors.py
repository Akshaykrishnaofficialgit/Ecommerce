from cart.models import Cart
def count_items(request):
    count=0
    u=request.user
    if request.user.is_authenticated:
        c=Cart.objects.filter(user=u)
        for i in c:
            count+=1
    return {'count':count}
