from django.db import models

class Apps(models.Model):
    AppName=models.CharField(max_length=100)
    AppLink=models.CharField(max_length=100)
    AppCategory=models.CharField(max_length=100,default="Entertainment")
    subcategory=models.CharField(max_length=100,default="SocialMedia")
    AppImage=models.URLField(blank=True)
    Points=models.IntegerField()
    def __str__(self):
        return self.AppName
class Users(models.Model):
    type=(
        ("owner","owner"),
        ("user","user")
    )
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    type=models.CharField(max_length=12,choices=type,default="user")
    def __str__(self):
        return self.username
class Transactions(models.Model):
    AppId=models.IntegerField(unique=True)
    UserId=models.IntegerField()
    Image=models.ImageField(blank=False)
    TransactionPoints=models.IntegerField()
class ActiveUser(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=50)
    def __str__(self):
        return self.username