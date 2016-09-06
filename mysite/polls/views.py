from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# # Create your views here.
# # def index(request):
# #     latest_questions = Question.objects.order_by('-pub_date')[0:5]
# #     template = loader.get_template('polls/index.html')
# #     context = {'latest_questions':latest_questions, }
# #     return HttpResponse(template.render(context,request))

# # render() shortcut
# def index(request):
#     latest_questions = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_questions':latest_questions}
#     return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''Return the last five published questions!!'''
        return Question.objects.order_by('-pub_date')[:5]


def latest(request):
    latest_questions = Question.objects.order_by('-pub_date')[0:5]
    output = '<br>'.join([q.question_text for q in latest_questions])
    return HttpResponse(output)



# # def detail(request, question_id):
# #     try:
# #         q = Question.objects.get(id=question_id)
# #         output = "You're looking at question %s. which is: <br>%s" % (question_id,q.question_text)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return HttpResponse(output)
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})
class DetailView(generic.ListView):
    model = Question
    template_name = 'polls/detail.html' # django automaticaly assign template_name to '<app name>/<model name>_detail.html'
                                        # so template_name='polls/question_detail.html' by default


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})
class ResultsView(generic.ListView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':'you didnt select anything!!'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question.id])) 
        # if you need to use somthing similar to the url template tag in your code, Django provides reverse()
        # reverse(viewname, urlconf=None, kwargs=None, current_app=None)



