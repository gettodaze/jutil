from django.urls import path
from renraku.polls import views

app_name = "polls"
# fmt: off
urlpatterns = [
    path("",                            views.IndexView.as_view(), name="index"),
    path("<int:pk>/",                   views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/",           views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/",     views.vote, name="vote"),
    path("question/add/",               views.QuestionCreateView.as_view(), name="question-add"),
    path("question/<int:pk>/",          views.QuestionUpdateView.as_view(), name="question-update"),
    path("question/<int:pk>/delete/",   views.QuestionDeleteView.as_view(),name="question-delete"),
    path("choice/add/",                 views.ChoiceCreateView.as_view(), name="choice-add"),
    path("choice/<int:pk>/",            views.ChoiceUpdateView.as_view(), name="choice-update"),
    path( "choice/<int:pk>/delete/",    views.ChoiceDeleteView.as_view(), name="choice-delete"),
]
# fmt: on
