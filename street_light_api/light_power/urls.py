from django.urls import path
from light_power import views

urlpatterns=[
    path('',views.index, name='index')
    path('',views.display, name='display')
]
