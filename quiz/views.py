from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index(request):
  tests = Test.objects.all()
  return render(request,'quiz/index.html',{'tests':tests})

@login_required(login_url='login')
def ready_to_test(request,test_id):
  test = get_object_or_404(Test,id=test_id)
  return render(request,'quiz/ready_to_test.html',{'test':test})

@login_required(login_url='login')
def test(request,test_id):
  test = get_object_or_404(Test,id=test_id)
  attemps = CheckTest.objects.filter(student=request.user,test=test).count()
  if (timezone.now() >= test.start_date and timezone.now() <= test.end_date) and attemps<test.maximum_attempts:
    questions = Question.objects.filter(test=test)
    if request.method == "POST":
      checktest = CheckTest.objects.create(student=request.user,test=test)
      for question in questions:
        given_answer = request.POST[str(question.id)]
        CheckQuestion.objects.create(checktest=checktest,question=question,given_answer=given_answer,true_answer=question.true_answer,)
      checktest.save()
      return redirect('checktest',checktest.id)
    context = {'test':test, 'questions': questions}
    return render(request,'quiz/test.html',context)
  else:
    return HttpResponse('Urinishlar soni yoki vaqt tugadi')

@login_required(login_url='login')
def checktest(request,checktest_id):
  checktest = get_object_or_404(CheckTest,id=checktest_id, student=request.user)
  return render(request,'quiz/checktest.html',{'checktest':checktest})