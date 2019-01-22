#you have to create this file urls.py

from django.urls import path

from . import views

#lets specify the app name as your url names can be use for other apps.
#you should specify as well this app name on your url name tags in your template
app_name = 'polls'
# urlpatterns = [
#     #the name or 3rd parameter is very useful in your template file in using the {% url %} template tag
#     path('', views.index, name='index'), #/polls/
#     path('<int:question_id>/', views.detail, name='detail'), #/polls/3
#     path('<int:question_id>/results/', views.results, name='results'), #/polls/3/results/
#     path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/3/vote/
#
# ]
urlpatterns = [
    #the name or 3rd parameter is very useful in your template file in using the {% url %} template tag
    path('', views.IndexView.as_view(), name='index'), #/polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #/polls/3
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), #/polls/3/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), #/polls/3/vote/

]
