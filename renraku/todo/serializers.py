from renraku.todo.models import TodoTask
from rest_framework import serializers


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ("id", "title", "description", "completed")
