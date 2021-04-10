from django.contrib import admin
from django.urls import path
from exerciseapp.views import (
    exercise_detail,
    ExerciseListView,
    ExerciseListView2,
    ExerciseCreateView
)
import random

random_pk = random.randint(1,3)
print(random_pk)
urlpatterns = [
    path('', ExerciseListView2.as_view(),name="exercise-list"),
    path('card/', ExerciseListView2.as_view(),name="exercise-list2"),
    path('random/', exercise_detail,{'pk':random_pk},name="exercise-detail"),
    path('<int:pk>/', exercise_detail,name="exercise-detail"),
    path('create/', ExerciseCreateView.as_view(),name="exercise-create"),
]

