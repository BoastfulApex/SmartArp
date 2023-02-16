from django.urls import path
from .views import *

urlpatterns = [
    # path('plan_create/', plan_create, name='plan_create'),
    # path('add_post/', add_post, name='add_post'),
    path('', main, name='main')
]
