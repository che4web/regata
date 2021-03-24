"""newregata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from exerciseapp.views import exercise_list,exercise_detail,home,ExerciseListView,ExerciseListView2

from competitionsapp.views import answer_create,score_table,simple_ajax
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from exerciseapp.admin import admin_site

urlpatterns = [
    path('', home),
    #path('exercise/', exercise_list),
    path('exercise2/', ExerciseListView2.as_view(),name="exercise-list2"),
    path('exercise/', ExerciseListView.as_view(),name="exercise-list"),
    path('exercise/<int:pk>/', exercise_detail,name="exercise-detail"),
    path('aswer/create', answer_create,name="answer-create"),
    path('score_table/', score_table,name="score_table"),
    path('admin/', admin_site.urls),
    path('simple_ajax', simple_ajax),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
