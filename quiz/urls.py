from django.urls import path
from .views import *
from .user_views import profile

urlpatterns = [
  # other urls
  path('test/',index,name='index'),
  # test urls
  path('<int:test_id>/ready_to_test',ready_to_test,name='ready_to_test'),
  path('<int:test_id>/test',test,name='test'),
  path('<int:checktest_id>/checktest',checktest,name='checktest'),
  # user urls
  path('<int:user_id>/profile',profile,name='profile'),
]