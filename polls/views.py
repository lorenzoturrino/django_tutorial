from django.shortcuts import render
from django.http import HttpResponse
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

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question %s."
    return HttpResponse(response % question_id)
