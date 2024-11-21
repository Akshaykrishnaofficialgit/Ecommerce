from django.urls import path
from shop import views
app_name="shop"
urlpatterns=[
    path('',views.categories,name="categories"),
    path('products/<int:i>',views.products,name="products"),
    path('productdetail/<int:i>',views.productdetail,name="productdetail"),
    path('register',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('addcategory',views.add_category,name='addcategory'),
    path('addproduct',views.add_product,name='addproduct'),
    path('addobject/<int:pro>/', views.add_object, name='addobject')
]