from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('product/add_product', views.add_product, name='add_product'),
    # path('product/product_edit/<int:id>/', views.edit_product, name='product_edit'),
    path('product/delete/<int:id>', views.delete_product, name='delete_product'),
    path('create/', views.ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='update_product'),
    path('count/', views.sum_count, name='sum_count'),
    path('time_product/', views.time_product, name='time_product'),
    path('create_manufacturer/', views.create_manufacturer, name='create_manufacturer'),
    path('selection_manufacturer/', views.selection_manufacturer, name='selection_manufacturer'),
    path('discount_search/', views.discount_search, name='discount_search'),
]
