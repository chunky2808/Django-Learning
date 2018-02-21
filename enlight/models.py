from django.db import models
from django.contrib.auth.models import User


class enli(models.Model):
	name = models.CharField(max_length = 50,unique=True)
	desc = models.CharField(max_length = 150)		

class topic(models.Model):
	subject = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now_add=True)
	



class Post(models.Model):
	message = models.TextField(max_length = 1000)
