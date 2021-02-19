from django.contrib import admin
from exerciseapp.models import Exercise
# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id','name','text','score']
    search_fields = ['name','text']


