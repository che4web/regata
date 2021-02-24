from django.shortcuts import render
from django.http import  HttpResponse

from exerciseapp.models import Exercise
from competitionsapp.models import Answer
from competitionsapp.forms import AnswerForm

# Create your views here.

def home(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'home.html',context)


def exercise_list(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'exercise_list.html',context)


def exercise_detail(request,pk):
    exercise = Exercise.objects.get(id=pk)
    context ={'exercise':exercise}
    if request.method == "POST":
        team = request.user.team
        form =  AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.team =team
            answer.exercise= exercise
            answer.save()
            context['success']='Ваш ответ принять'

        else:
            context['form']=form
    else:
        context['form'] =  AnswerForm(initial={'exercise':exercise.id})



    return render(request,'exercise_detail.html',context)




