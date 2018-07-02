from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#继承修改用户表


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), max_length=10, default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
