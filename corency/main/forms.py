from django import forms
from .models import Coins

class PostForm(forms.ModelForm) :
    class Meta :
        model = Coins
        fields = ["name","apiurl","logourl","discription"]