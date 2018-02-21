from django.shortcuts import render
from django.http import HttpResponse
from .models import Forum

# Create your views here.
def home(request):
	forums = Forum.objects.all()
	return render(request,'home.html',{'forums' : forums})
