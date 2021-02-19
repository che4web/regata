from django.shortcuts import render
from django.http import  HttpResponse

from exerciseapp.models import Exercise


# Create your views here.

def exercise_list(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'exercise_list.html',context)

def exercise_detail(request,pk):
    exercise = Exercise.objects.get(id=pk)
    context ={'exercise':exercise}
    return render(request,'exercise_detail.html',context)




