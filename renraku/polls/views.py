import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from renraku.polls.models import Question


# Create your views here.
def index(_: HttpResponse) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    questions = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(f"Welcome to polls!\n{questions}")


def detail(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} detail.")


def results(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} results.")


def vote(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} voting.")
