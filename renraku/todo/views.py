from django.shortcuts import render
from renraku.todo.models import TodoTask
from renraku.todo.serializers import TodoTaskSerializer
from rest_framework import viewsets


# Create your views here.
class TodoTaskView(viewsets.ModelViewSet):
    serializer_class = TodoTaskSerializer
    queryset = TodoTask.objects.all()
