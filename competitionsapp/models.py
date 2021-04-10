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
    def answer_count(self):
        return self.answer_set.all().count()

class Answer(models.Model):
    team = models.ForeignKey(Team,verbose_name='Комманда',on_delete=models.CASCADE,null=True)
    value = models.CharField(max_length=255,verbose_name='Ответ')
    exercise = models.ForeignKey(Exercise,verbose_name='Задача',on_delete=models.PROTECT)
    correct = models.BooleanField(blank=True,default=False)
    def exercise_answer(self):
        return self.exercise.true_answer
    class Meta:
        unique_together = [
            ['team','exercise'],
        ]

class Raund(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    exercise = models.ManyToManyField(Exercise,blank=True)
    STATUS_CHOICEN= (
        ("NO",'Не активен'),
        ("ON",'В игре'),
        ("DO",'Завершен'),
    )
    status = models.CharField(max_length=2,default="NO",choices=STATUS_CHOICEN)

class Judge(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название")
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Grade(models.Model):
    judge = models.ForeignKey(Judge,verbose_name="Судья",on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,verbose_name='Ответ',on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name="Оценка")
