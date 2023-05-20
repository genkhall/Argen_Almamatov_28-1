from django.db import models


# Create your models here.


# class Post(models.Model):
#     image = models.ImageField(null=True, blank=True)
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#     rate = models.FloatField(default=0)
#
#     def __str__(self):
#         return self.title

class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=200)
    model = models.CharField(max_length=150)
    color = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=250)
    comment = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment.title} - {self.text}'

