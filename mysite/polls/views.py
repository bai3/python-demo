from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('_pub_data')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def result(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)