from django.db import models

# Create your models here.

class Items(models.Model):
    
    def __str__(self): 
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_disc = models.IntegerField()
   
    #you may need to migrate the server to initialize the whold structure to your settings's installed apps to initialize the dbs
    