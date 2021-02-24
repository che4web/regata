from django.db import models
from django.contrib.auth.models import User
from exerciseapp.models import Exercise

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    shcool = models.CharField(max_length=255,verbose_name="Школа")
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name +'. ' +self.shcool

class Answer(models.Model):
    team = models.ForeignKey(Team,verbose_name='Комманда',on_delete=models.CASCADE,null=True)
    value = models.CharField(max_length=255,verbose_name='Ответ')
    exercise = models.ForeignKey(Exercise,verbose_name='Задача',on_delete=models.PROTECT)
