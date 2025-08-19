from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Coins
from .forms import PostForm
# Create your views here.


def home(request) :
    coins = Coins.objects.all()
    return render(request , "home.html" , {"coins" : coins})

def cointInfi(request , name) : 
    coin = get_object_or_404(Coins , name = name)
    return render(request , "coinInfo.html" , {'coin' : coin})


def addCoint(request) : 
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("add-coin")
    else :
        form = PostForm()
    return render(request , "addcoint.html" , {"form" : form})