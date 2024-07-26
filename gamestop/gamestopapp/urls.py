from django.urls import path
from gamestopapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('create_product', views.create_product),
    path('read',views.read),
    path('delete/<rid>',views.delete),
    path('update/<rid>',views.update),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('create_cart/<rid>', views.create_cart),
    path('read_cart',views.read_cart),
    path('delete_cart/<rid>',views.delete_cart),
    path('update_cart/<rid>/<q>', views.update_cart),
    path('create_orders/<rid>',views.create_orders),
    path('read_order',views.read_order),
    path('create_review/<rid>',views.create_review),
    path('read_product_detail/<rid>',views.read_product_detail),
    path('forget_password', views.forget_password),
    path('otp_verification',views.otp_verification),
    path('new_password',views.new_password),
    path('search_product',views.search_product)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)