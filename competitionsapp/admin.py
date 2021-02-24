from django.contrib import admin
from competitionsapp.models import Team,Answer

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines=[
        AnswerInline
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


