from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import  get_user_model

# User = get_user_model()
class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)

class Name(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(verbose_name='作成日時',default=timezone.now)

    
class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Comfort(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SettingSize(models.Model):
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )
    name = models.CharField('服の名前',max_length=150,blank=False)
    type =models.ForeignKey(Type, on_delete=models.CASCADE,default='',blank=False)
    body_length = models.PositiveIntegerField("着丈", blank=True,)
    chest = models.PositiveIntegerField("胸囲",blank=True, )
    shoulder = models.PositiveIntegerField("肩幅", blank=True, )
    arm = models.PositiveIntegerField("袖丈", blank=True, )
    comfort = models.ForeignKey(Comfort, on_delete=models.CASCADE,default='',blank=False)
    def __str__(self):
        return self.name



   


 