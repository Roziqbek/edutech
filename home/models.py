from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactModel(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  tel = models.BigIntegerField()
  text = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

class VideoModel1(models.Model):
  teacher = models.CharField(max_length=100)
  caption = models.CharField(max_length=100)
  img = models.ImageField(upload_to='img')
  video = models.FileField(upload_to='video')
  doc = models.FileField(upload_to='doc')
  date = models.DateTimeField()

  def __str__(self):
    return self.caption