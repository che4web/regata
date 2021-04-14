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
from django.urls import path,re_path,include
from exerciseapp.views import home,ExerciseViewSet

from competitionsapp.views import answer_create,score_table,simple_ajax
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
#from exerciseapp.admin import admin_site
from rest_framework import routers
router =  routers.DefaultRouter()
router.register('exercise',ExerciseViewSet)

urlpatterns = [
    path('', home),
    path('api/',include(router.urls)),
    path('exercise/',include('exerciseapp.urls')),
    path('competitions/',include('competitionsapp.urls')),
    path('admin/', admin.site.urls,name="admin-main"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
