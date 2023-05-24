from django.urls import path
from .views import *

urlpatterns = [
  path('',AboutPage,name='about'),
  path('login/',Login,name='login'),
  path('signup/',signup,name='signup'),
  path('logout/',LogOut,name='logout'),

  path('courses/',CoursesPage,name='courses'),
  path('courses/playlist/',PlaylistPage,name='playlist'),
  path('courses/playlist/<str:name>',Watch_videoPage,name='watch_video'),

  path('contact/',ContactPage,name='contact'),
]