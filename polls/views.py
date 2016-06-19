from django.shortcuts import render
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    pars = {
        'latest_questions': latest_questions,
    }
    return render(request, 'polls/index.html', pars)

    # template = loader.get_template('polls/index.html')
    # output = template.render(pars, request)
    # return HttpResponse(output)

def detail(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Invalid question id")
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
