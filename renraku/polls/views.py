from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from renraku.polls.models import Choice, Question


class QuestionCreateView(generic.edit.CreateView):
    model = Question
    fields = ["question_text", "pub_date"]

    def get_success_url(self):
        return reverse("polls:index")


class QuestionUpdateView(generic.edit.UpdateView):
    model = Question
    fields = ["question_text"]

    def get_success_url(self):
        return reverse("polls:index")


class QuestionDeleteView(generic.edit.DeleteView):
    model = Question
    success_url = reverse_lazy("polls:index")


class ChoiceCreateView(generic.edit.CreateView):
    model = Choice
    fields = ["choice_text", "question"]

    def get_success_url(self):
        return reverse("polls:index")


class ChoiceUpdateView(generic.edit.UpdateView):
    model = Choice
    fields = ["choice_text", "question", "votes"]

    def get_success_url(self):
        return reverse("polls:index")


class ChoiceDeleteView(generic.edit.DeleteView):
    model = Choice
    success_url = reverse_lazy("polls:index")


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
