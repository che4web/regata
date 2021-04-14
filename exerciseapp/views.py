from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from exerciseapp.models import Exercise
from exerciseapp.serializers import ExerciseSerializer

from django.contrib.auth.mixins import LoginRequiredMixin

from competitionsapp.models import Answer,Raund
from competitionsapp.forms import AnswerForm
from rest_framework import viewsets

# Create your views here.

def home(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    return render(request,'home.html',context)

@login_required
def exercise_list(request):
    exercise_list = Exercise.objects.exclude(raund__status="NO")
    context ={'exercise_list':exercise_list}
    return render(request,'exercise_list.html',context)

class MyListView(LoginRequiredMixin,ListView):
    pass
class ExerciseListView(MyListView):
    model = Exercise
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['raund'] = Raund.objects.all()
        return context
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.has_perm('exerciseapp.some_prem'):
            return queryset.exclude(raund__status="NO")
        else:
            return self.model.objects.none()


class ExerciseListView2(ListView):
    model = Exercise
    template_name="exerciseapp/exercise_list2.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(raund__status="NO")

class ExerciseCreateView(CreateView):
    model =Exercise
    fields = "__all__"

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
            messages.success(request,"MESSAGE:Ответ успешно принять")

            return redirect('exercise-list')
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



class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset =super().get_queryset()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset
