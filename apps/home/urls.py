# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('plan_create/', views.plan_create, name='plan_create'),
    path('add_post/', views.add_post, name='add_post'),
    # path('slider_create/', views.slider_create, name='slider_create'),
    # path('sliders/<int:pk>', views.slider_detail, name='slider_detail'),
    # path('slider_delete/<int:pk>', views.SliderDelete.as_view(), name='slider_delete'),
    # path('categories/', views.categories, name='categories'),
    # path('category_create/', views.category_create, name='category_create'),
    # path('category/<int:pk>', views.category_detail, name='category_detail'),
    # path('product_by_category/<int:pk>', views.product_by_category, name='product_by_category'),
    # path('category_delete/<int:pk>', views.CategoryDelete.as_view(), name='category_delete'),
    # path('brands/', views.brands, name='brands'),
    # path('brand_create/', views.brand_create, name='brand_create'),
    # path('brand/<int:pk>', views.brand_detail, name='brand_detail'),
    # path('product_by_brand/<int:pk>', views.product_by_brand, name='product_by_brand'),
    # path('brand_delete/<int:pk>', views.BrandDelete.as_view(), name='brand_delete'),
    # path('products', views.products, name='products'),
    # path('product_create', views.product_create, name='product_create'),
    # path('product/<int:pk>', views.product_detail, name='product_detail'),
    # path('product_delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
    # path('types/', views.types, name='types'),
    # path('types/<int:pk>', views.type_detail, name='type_detail'),
    # path('product_by_type/<int:pk>', views.product_by_type, name='product_by_type'),
    # path('type_create/', views.type_create, name='type_create'),
    # path('type_delete/<int:pk>', views.TypeDelete.as_view(), name='type_delete'),
    # path('color_create/<int:pk>', views.color_create, name='color_create'),
    # path('color_delete/<int:pk>', views.ColorDelete.as_view(), name='color_delete'),
]
