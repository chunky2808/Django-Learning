from django.shortcuts import render
from django.http import HttpResponse
from .models import Forum

# Create your views here.
def home(request):
	forums = Forum.objects.all()
	forum_name = list()

	for forum in forums:
		forum_name.append(forum.name)

	response_html = '<br>'.join(forum_name)	
	return HttpResponse(response_html)
