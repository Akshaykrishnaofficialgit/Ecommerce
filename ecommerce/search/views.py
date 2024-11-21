from django.shortcuts import render
from django.db.models import Q
from shop.models import Products
def search_products(request):
    p=None
    query=""
    if (request.method=="POST"):
        query=request.POST['sss']
        if query:
            p=Products.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    params={'pro':p,'query':query}
    return render(request,'search.html',params)
