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

class Raund(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    exercise = models.ManyToManyField(Exercise,blank=True)

class Judge(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Grade(models.Model):
    judge = models.ForeignKey(Judge,verbose_name="Судья",on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,verbose_name='Ответ',on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Оценка")
