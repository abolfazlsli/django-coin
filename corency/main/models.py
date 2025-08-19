from django.db import models

class Coins(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    apiurl = models.CharField(max_length=200)            
    logourl = models.CharField(max_length=200)           
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
