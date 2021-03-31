from django.contrib import admin
from competitionsapp.models import Team,Answer,Grade,Judge,Raund

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


@admin.register(Raund)
class RaundAdmin(admin.ModelAdmin):
    pass
@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

