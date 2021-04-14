from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
def path_to_upload(instance,filename):
    return 'exercise/{0}/{1}'.format(instance.id, filename)

class Exercise(models.Model):
    TYPE_CHOICES=(
        ('I','требует ответа в виде целого числа'),
        ('B','Да или нет'),
        ('F','Развернутый ответ'),
         )
    typ= models.CharField(choices=TYPE_CHOICES,blank=True,default='F',max_length=1)
    name = models.CharField(max_length=255,verbose_name="Название задачи")
    text = models.TextField(verbose_name="Полный текст задачи в формате LaTeX")
    solution = models.TextField(
        verbose_name="Полный текст решения в формате LaTeX",
        blank=True
    )
    true_answer = models.CharField(verbose_name="Правильный ответ",max_length=255,blank=True)
    score = models.IntegerField(blank=True,default=0)
    image = ThumbnailerImageField(blank=True,null=True,upload_to='exercise/')
    def get_preview(self):
        if self.image:
            return self.image['preview'].url
        else:
            return ''
    def get_absolute_url(self):
        return reverse('exercise-detail',args=[self.id])

    def __str__(self):
        return self.name
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return 'defaul.png'
    def admin_t(self):
        if self.image:
            return mark_safe('<img src="{}">'.format(self.image['preview'].url))
        else:
            return 'нет картинки'
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        permissions = [
            ('some_prem',' Мое право')
        ]
