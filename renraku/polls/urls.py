from django.urls import path
from renraku.polls import views

urlpatterns = [path("", views.index, name="index")]
