from django.shortcuts import render
from exerciseapp.models import Exercise
from competitionsapp.models import Team,Grade,Raund
from django.db.models import Sum,Q,Count
from django.http import JsonResponse

import json
# Create your views here.
def answer_create(request):
    return None


def score_table(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    team_list = Team.objects.all()
    context['team_list'] = team_list
    context['raund_list'] = Raund.objects.all().annotate(Count('exercise'))
    table=[]
    team_list2 = team_list.values('id','name','answer__exercise').annotate(score=Sum('answer__grade__value'))
    team_list3 = team_list.values('id','name').annotate(score=Sum('answer__grade__value'))
    for team in team_list:
        tmp= team_list2.filter(id=team.id)
        row = [team.name]
        for t in tmp:
            row.append(t['score'])

        tmp= team_list3.filter(id=team.id)
        row.append(tmp[0]['score'])


        table.append(row)

    context['score_table'] = table

    return render(request,'score_table.html',context)

def simple_ajax(request):
    data  = json.loads(request.body.decode('utf-8'))
    text = data['text']
    return JsonResponse({'data':text})
