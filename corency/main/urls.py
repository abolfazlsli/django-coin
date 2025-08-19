from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home") ,
    path("coininfo/<str:name>/" , views.cointInfi , name="coininfo") ,
    path("add-coin" , views.addCoint , name="add-coin" )

]