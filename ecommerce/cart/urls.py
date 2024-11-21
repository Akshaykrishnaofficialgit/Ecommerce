from django.urls import path
from cart import views
app_name="cart"
urlpatterns=[
    path('add_to_cart/<int:i>',views.add_to_cart,name="add_to_cart"),
    path('cartview/',views.cart_view,name="cartview"),
    path('removeitem/<int:i>',views.remove_item,name="removeitem"),
    path('trash/<int:i>',views.trash,name="trash"),
    path('checkout',views.checkout,name="checkout"),
    path('payment_status/<str:p>',views.payment_status,name="status"),
    path('your_orders',views.your_orders,name="yourorders"),
]