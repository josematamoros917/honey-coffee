from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/<int:category_id>/', views.productos, name='product_list_by_category'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_view, name='contact_us'),
    path('contact/success/', views.contact_success, name='contact_success'),
    # path('store/<int:store_id>/', views.store_detail, name='store_detail'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('social_media/<int:social_media_id>/', views.social_media_detail, name='social_media_detail'),
]
