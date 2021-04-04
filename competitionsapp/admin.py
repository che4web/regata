from django.contrib import admin
from competitionsapp.models import Team,Answer,Grade,Judge,Raund
#from exerciseapp.admin import admin_site

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer

class TeamAdmin(admin.ModelAdmin):
    inlines=[
        AnswerInline
    ]
    list_display = ('id','name','shcool','answer_count',)
    list_editable = ('name',)
    list_filter =('shcool','name')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','team','exercise','value','exercise_answer','correct')
    list_editable = ('correct',)
    pass


class RaundAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_editable = ('status',)
    pass
class JudgeAdmin(admin.ModelAdmin):
    pass

class GradeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grade,GradeAdmin)
admin.site.register(Raund,RaundAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Answer,AnswerAdmin)
