from django.db import models
from django.contrib.auth.models import User 
import datetime  
import os 

def getFileName(request, filename):  
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)
# def file create for static folder la uploads folder la irukka images get panna
class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    #upload files go to (def - getfilename )static folder-> uploads file 
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")   
    # Boolean Tag used for insert check box 
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  #Foreinkey to join or link two tables together
  # Casecade for  deleting the reference object will also delete the referred object.
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.FloatField(null=False,blank=False)
  selling_price=models.FloatField(null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name
    
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)


  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price

class Favourite(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)