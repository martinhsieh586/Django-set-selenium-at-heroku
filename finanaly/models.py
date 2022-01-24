from django.db import models

#會員資料表
class user(models.Model):
    username = models.CharField(max_length=20,null=False,unique=True)
    useremail = models.EmailField(max_length=100,null=False,unique=True)
    userpassword = models.CharField(max_length=20,null=False,unique=True)

#會員收藏資料庫
class pocket(models.Model):
    username = models.CharField(max_length=20,null=True,unique=False)
    url = models.CharField(max_length=200,null=True,unique=True)
    name = models.CharField(max_length=50,null=True,unique=False)

#電商平台資料表
class bussinessinfo(models.Model):
    name = models.CharField(max_length=20,null=False,unique=True)
    category = models.CharField(max_length=20,null=False)
