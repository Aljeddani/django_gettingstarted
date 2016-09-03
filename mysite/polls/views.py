from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice


# Create your views here.
# def index(request):
#     latest_questions = Question.objects.order_by('-pub_date')[0:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_questions':latest_questions, }
#     return HttpResponse(template.render(context,request))

# render() shortcut
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions':latest_questions}
    return render(request, 'polls/index.html', context)


def latest(request):
    latest_questions = Question.objects.order_by('-pub_date')[0:5]
    output = '<br>'.join([q.question_text for q in latest_questions])
    return HttpResponse(output)


# def detail(request, question_id):
#     try:
#         q = Question.objects.get(id=question_id)
#         output = "You're looking at question %s. which is: <br>%s" % (question_id,q.question_text)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return HttpResponse(output)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = get_list_or_404(Choice, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question,'choices':choices})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id) 


def vote(request, question_id):
    return HttpResponse('You are voting on question %s ' % question_id)


