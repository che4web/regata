from django.shortcuts import render
from exerciseapp.models import Exercise
from competitionsapp.models import Team,Grade
from django.db.models import Sum,Q
# Create your views here.
def answer_create(request):
    return None


def score_table(request):
    exercise_list = Exercise.objects.all()
    context ={'exercise_list':exercise_list}
    team_list = Team.objects.all()
    context['team_list'] = team_list
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


        #for exercise in exercise_list:
        #    answer_list = Grade.objects.filter(
        #        answer__exercise=exercise,
        #        answer__team=team)
        #    score = answer_list.aggregate(Sum('value'))['value__sum']
        #score_list = exercise_list.value().annotate(total_score=Sum('answer__grade__value'))
        #for score in score_list:
        #    row.append(score.total_score)
        table.append(row)

    context['score_table'] = table

    return render(request,'score_table.html',context)
