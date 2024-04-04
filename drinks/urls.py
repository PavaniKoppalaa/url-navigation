from django.urls import path
from drinks.views import *
app_name='drinks'
urlpatterns=[
    path('maaza/',maaza,name='maaza'),
    path('sprite/',sprite,name='sprite'),
]