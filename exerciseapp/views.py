from django.shortcuts import render
from django.http import  HttpResponse

from django.contrib.auth.decorators import login_required
from exerciseapp.models import Exercise
from competitionsapp.models import Answer
from competitionsapp.forms import AnswerForm

# Create your views here.

def home(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'home.html',context)

@login_required
def exercise_list(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'exercise_list.html',context)


@login_required
def exercise_detail(request,pk):
    exercise = Exercise.objects.get(id=pk)
    context ={'exercise':exercise}
    if hasattr(request.user,'team'):
        team = request.user.team
    else:
        team =None
    if hasattr(request.user,'judge'):
        judge = request.user.judge
    else:
        judge= None
    if request.method == "POST":
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
        if team:
            answer = exercise.answer_set.filter(team=team).first()
            context['answer'] =answer
        if judge:
            answer_list = exercise.answer_set.all()
            for x in answer_list:
                x.my_grade = x.grade_set.filter(judge=judge).first()
            context['answer_list']= answer_list

        context['form'] =  AnswerForm(initial={'exercise':exercise.id})

    context['team']=team

    return render(request,'exercise_detail.html',context)




