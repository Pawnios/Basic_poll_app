from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import question_cls,choice_cls
from django.template import loader
from django.urls import reverse

# Create your views here.

def index(request): #displays latest 5 questions
    latest_question_list = question_cls.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question=question_cls.objects.get(pk=question_id)
    except question_cls.DoesNotExist:
           raise Http404("question doesnt exits")
    return render(request,'details.html', {'question':question})

def results(request, question_id):
    question=get_object_or_404(question_cls,pk=question_id)
    return render(request, 'results.html', {
              'question':question,
              })
   


def vote(request, question_id):
    question=get_object_or_404(question_cls,pk=question_id)

    try:
         selected_choice=question.choice_cls_set.get(pk=request.POST['choice'])

    except(KeyError,choice_cls.DoesNotExist):
         return render(request, 'detail.html', {
              'question':question,
              'error_message':"you didnt select a choice",
         })
    else:
         selected_choice.votes+=1
         selected_choice.save()

         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))