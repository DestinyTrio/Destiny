from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:career_detail>/',
         views.careerDetail, name="careerDetail"),
    path('<slug:career_detail>/form', views.careerForm, name='careerForm'),

]
