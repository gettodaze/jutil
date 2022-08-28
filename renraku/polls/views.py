import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse("index content! Hello AD! Hello Dausie!!!! ")


def detail(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} detail.")


def results(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} results.")


def vote(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"question {question_id} voting.")
