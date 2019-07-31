from django.urls import path
from . import views
from .apiviews import AppViewSet, ChoiceList, CreateVote, UserCreate, LoginView

urlpatterns = [
    path('App2/', views.index, name ='index2'),
    path("login/", LoginView.as_view(), name="login"),

]
