from django.shortcuts import render
from exerciseapp.models import Exercise
from competitionsapp.models import Team,Grade,Raund,Answer
from django.db.models import Sum,Q,Count
from django.http import JsonResponse
from competitionsapp.serializers import AnswerSerializer

from rest_framework import viewsets
import json
# Create your views here.
def answer_create(request):
    return None


def score_table(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    team_list = Team.objects.all()
    context['team_list'] = team_list
    raund_list = Raund.objects.all().annotate(Count('exercise'))
    context['raund_list'] = raund_list
    table=[]
    team_list2 = team_list.values(
            'id',
            'name',
            'answer__exercise'
        ).annotate(score=Sum(
            'answer__exercise__score',
            filter=Q(answer__correct=True)))
    team_list3 = team_list.values('id','name').annotate(score=Sum('answer__grade__value'))
    for team in team_list:
        row = [team.name]
        for r in raund_list:
            for e in r.exercise.all():
                answer =  e.answer_set.filter(team=team).first()
                if answer:
                    if answer.correct:
                        row.append(answer.exercise.score)
                    else:
                        row.append(0)

                else:
                    row.append('')

        tmp= team.answer_set.filter(correct=True).aggregate(score=Sum('exercise__score'))
        row.append(tmp['score'])


        table.append(row)

    context['score_table'] = table

    return render(request,'score_table.html',context)

def simple_ajax(request):
    data = json.loads(request.body.decode('utf-8'))
    if data['id']:
        grade = Grade.objects.get(id=data['id'])
        grade.value= data['value']
        grade.save()
    else:
        data.pop('id')
        data['judge'] = request.user.judge
        grade = Grade(**data)
        grade.save()
    return JsonResponse({'id':grade.id,'answer':grade.answer.id})

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

