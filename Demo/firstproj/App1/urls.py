from django.urls import path
from . import views

urlpatterns=[
    path('App1/',views.index1,name='index1'),
]
