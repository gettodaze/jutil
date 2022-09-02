from django.contrib import admin
from renraku.polls.models import Choice, Question
from renraku.todo.models import TodoTask


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")


class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")


# Register your models here.

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(TodoTask, TodoTaskAdmin)
