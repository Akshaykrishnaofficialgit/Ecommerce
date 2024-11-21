from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def categories(requests):
    c=Category.objects.all()
    context={'cat':c}
    return render(requests,'categories.html',context)

@login_required
def products(requests,i):
    ce=Category.objects.get(id=i)
    p=Products.objects.filter(category=ce)
    context={'cat':ce,'pro':p}
    return render(requests,'products.html',context)

@login_required
def productdetail(requests,i):
    p=Products.objects.get(id=i)
    context={'pro':p}
    return render(requests,'detail.html',context)


def register(request):
    if (request.method=="POST"):
        u=request.POST['un']
        f=request.POST['fn']
        e = request.POST['em']
        l = request.POST['ln']
        p = request.POST['pw']
        c = request.POST['cp']
        if p==c:
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
        else:
            return HttpResponse("Password did'nt match!")
        return redirect('shop:categories')
    return render(request,'register.html')

def user_login(request):
    if (request.method=="POST"):
            u=request.POST['un']
            p = request.POST['pa']
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('shop:categories')
            else:
                return HttpResponse("invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:login')


def add_category(request):
    if request.method=="POST":
        n=request.POST['cn']
        d=request.POST['de']
        i = request.FILES['im']
        u=Category.objects.create(name=n,desc=d,images=i)
        u.save()
        return redirect('shop:categories')
    return render(request,'add_category.html')

def add_product(request):
    if request.method=="POST":
        n=request.POST['cn']
        d=request.POST['de']
        i = request.FILES['imm']
        p=request.POST['pr']
        s=request.POST['st']
        c=request.POST['ct']
        cat=Category.objects.get(name=c)
        u=Products.objects.create(name=n,desc=d,image=i,price=p,stock=s,category=cat)
        u.save()
        return redirect('shop:categories')
    return render(request,'add_product.html')

def add_object(request,pro):
    p = Products.objects.get(id=pro)
    if (request.method=='POST'):
        p.stock=request.POST['cs']
        p.save()
        return redirect('shop:categories')
    context = {'pro': p}
    return render(request,'addobject.html',context)