from django.db import models

# Create your models here.

class Item(models.Model):
    
    def __str__(self): 
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_disc = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://www.foodservicerewards.com/cdn/shop/t/262/assets/fsr-placeholder.png?v=45093109498714503231652397781')
    #you may need to migrate the server to initialize the whold structure to your settings's installed apps to initialize the dbs
    