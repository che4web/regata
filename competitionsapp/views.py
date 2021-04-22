from django.shortcuts import render
from exerciseapp.models import Exercise
from competitionsapp.models import Team,Grade,Raund,Liga
from django.db.models import Sum,Q,Count
from django.http import JsonResponse

import json
# Create your views here.
def answer_create(request):
    return None


def score_table(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    liga_list = []
    for liga in Liga.objects.all():
        team_list = liga.team_set.all()
        team_list = team_list.annotate(score=Sum(
                'answer__exercise__score',
                filter=Q(answer__correct=True))).order_by('-score')
        context['team_list'] = team_list
        raund_list = Raund.objects.all().annotate(Count('exercise'))
        context['raund_list'] = raund_list
        table=[]
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
            row.append(tmp['score'] or 0)


            table.append(row)
        liga_list.append({'name':liga.name,'score_table':table})

    context['liga_list'] = liga_list

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
