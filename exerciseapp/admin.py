from django.contrib import admin
from exerciseapp.models import Exercise
# Register your models here.

#@admin.register(Exercise)
#class ExerciseAdmin(admin.ModelAdmin):
#    list_display = ['id','name','text','score']
#    search_fields = ['name','text']


class ExerciseAdmin2(admin.ModelAdmin):
    list_display = ['id','name','text','score','admin_t']
    search_fields = ['name','text']
    readonly_fields = ('admin_t',)


#from  django.contrib.admin  import  AdminSite
#class  MyAdminSite(AdminSite):
#    site_header =   'Физическая регата'

#admin.site = MyAdminSite(name="admin")
admin.site.register(Exercise,ExerciseAdmin2)
