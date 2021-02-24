from django.db import models
from django.urls import reverse

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название задачи")
    text = models.TextField(verbose_name="Полный текст задачи в формате LaTeX")
    solution = models.TextField(
        verbose_name="Полный текст решения в формате LaTeX",
        blank=True
    )
    true_answer = models.CharField(verbose_name="Правильный ответ",max_length=255,blank=True)
    score = models.IntegerField(blank=True,default=0)
    image = models.ImageField(blank=True,null=True)
    def get_absolure_url(self):
        return reverse('exercise-detail',args=[self.id])

    def __str__(self):
        return self.name
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'defaul.png'
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
