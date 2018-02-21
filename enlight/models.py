from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
	name = models.CharField(max_length = 50,unique=True)
	desc = models.CharField(max_length = 150)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now_add=True)
	forum = models.ForeignKey(Forum,related_name = 'topics')
	started_by = models.ForeignKey(User,related_name = 'topics')



class Post(models.Model):
	message = models.TextField(max_length = 1000)
	topic = models.ForeignKey(Topic,related_name='posts')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(null = True)
	created_by = models.ForeignKey(User,related_name='posts')
	updated_by = models.ForeignKey(User, null=True, related_name='+')