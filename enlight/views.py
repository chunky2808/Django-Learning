from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Forum

# Create your views here.
def home(request):
	forums = Forum.objects.all()
	return render(request,'home.html',{'forums' : forums})

def forum_topics(request,pk):
	forums = get_object_or_404(Forum, pk=pk)
	return render(request,'topics.html',{'forums': forums})