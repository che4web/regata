from django.contrib import admin
from django.urls import path,re_path,include
from exerciseapp.views import home

from competitionsapp.views import answer_create,score_table
from django.conf.urls.static import static

urlpatterns = [
    path('aswer/create', answer_create,name="answer-create"),
    path('score_table/<int:raund>/', score_table,name="score_table"),
    path('score_table/<foo>/', score_table,name="score_table"),
    path('score_table/', score_table,name="score_table"),
]
