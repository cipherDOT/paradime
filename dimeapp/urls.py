from django.urls import path
from .views import index, view, delete_question, delete_answer, update_question, update_answer, register, loginuser, logoutuser

urlpatterns = [
    path('',                       index,           name='index'),
    path('view/<str:key>/',        view,            name='view'),
    path('delete_ques/<str:key>/', delete_question, name='delete_question'),
    path('delete_ans/<str:key>/',  delete_answer,   name='delete_answer'),
    path('update_ques/<str:key>/', update_question, name='update_question'),
    path('update_ans/<str:key>/',  update_answer,   name='update_answer'),
    path('login/',                 loginuser,       name='login'),
    path('logout/',                logoutuser,      name='logout'),
    path('register/',              register,        name='register'),
]
