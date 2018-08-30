from django.urls import path

from dbmonitor import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run_all_validators', views.run_all_validators, name='run_all_validators'),
]