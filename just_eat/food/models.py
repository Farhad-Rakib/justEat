from turtle import mode
from django.db import models

class Restaurant(models.Model):
   name = models.CharField(max_length=50)
   location = models.CharField(max_length=250)
   description = models.TextField()
   rating = models.IntegerField()
   createdAt = models.DateTimeField(auto_now_add=True)

   class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

   def __str__(self):
        return self.name
   

class Category(models.Model):
   name = models.CharField(max_length=50)
   createdAt = models.DateTimeField(auto_now_add=True)

   class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

   def __str__(self):
        return self.name

class Item(models.Model):
   name = models.CharField(max_length=50)
   restaurant_id = models.ForeignKey(
      Restaurant, on_delete=models.SET_NULL, null=True, related_name='food_restaurant')
   category_id = models.ForeignKey(
      Category,on_delete=models.SET_NULL,null= True,        related_name='food_category')
   price = models.FloatField()
   description = models.TextField()
   rating = models.IntegerField()
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

   def __str__(self):
        return self.name


