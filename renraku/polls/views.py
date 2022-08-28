import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from renraku.polls.models import Question


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} detail.")


def results(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} results.")


def vote(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} voting.")
