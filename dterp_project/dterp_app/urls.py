from django.urls import path

from . import views

app_name = 'dterp'
urlpatterns = [
    path('', views.index, name='index'),

]
