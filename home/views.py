from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import FormWithCaptcha
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def AboutPage(request):
  user_count = User.objects.count()
  courses_count = VideoModel1.objects.count()
  return render(request, 'about.html',{'user_count':user_count,'courses_count':courses_count})

def signup(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    pass1 = request.POST.get('pass')
    pass2 = request.POST.get('c_pass')
    form = FormWithCaptcha(request.POST)
    if form.is_valid():
      if pass1 != pass2:
        return HttpResponse("Your password and cornfirm password are not same !!!")
      else:
        my_user = User.objects.create_user(name,email,pass1)
        my_user.save()
        return redirect('login')
    else:
      return HttpResponse('Are you robot ?')
  form = FormWithCaptcha()
  return render(request, 'register/signup.html',{'form':form})

def Login(request):
  if request.method == 'POST':
    name = request.POST.get('login_name')
    password = request.POST.get('login_pass')
    user = authenticate(request,username=name,password=password)
    if user is not None:
      login(request,user)
      return redirect('about')
    else:
      return HttpResponse("Username or Password is incorrect !!!")
  return render(request,'register/login.html')

@login_required(login_url='login')
def CoursesPage(request):
  video_count = VideoModel1.objects.count()
  return render(request, 'courses.html',{'video_count':video_count})

@login_required(login_url='login')
def PlaylistPage(request):
  video_dars = VideoModel1.objects.all()
  video_count = VideoModel1.objects.count()
  return render(request, 'playlist.html',{'video_dars':video_dars,'video_count':video_count})

@login_required(login_url='login')
def Watch_videoPage(request,name):
  denamic = VideoModel1.objects.get(caption=name)
  return render(request, 'watch-video.html',{'denamic':denamic})

@login_required(login_url='login')
def ContactPage(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    tel = request.POST.get('number')
    text = request.POST.get('text')
    obj = ContactModel(name=name,email=email,tel=tel,text=text)
    obj.save()
    return redirect('about')
  return render(request, 'contact.html')

@login_required(login_url='login')
def LogOut(request):
  logout(request)
  return redirect('about')