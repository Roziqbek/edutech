from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile(request, user_id):
  user =get_object_or_404(User,id=user_id)
  return render(request, 'profile.html',{'user':user})