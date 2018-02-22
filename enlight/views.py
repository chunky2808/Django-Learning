from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from .models import Forum,Topic,Post

# Create your views here.
def home(request):
	forums = Forum.objects.all()
	return render(request,'home.html',{'forums' : forums})

def forum_topics(request,pk):
	forums = get_object_or_404(Forum, pk=pk)
	return render(request,'topics.html',{'forums': forums})

def new_topic(request,pk):
	forums = get_object_or_404(Forum, pk=pk)
	if request.method == 'POST':
		subject = request.POST['subject']
		message = request.POST['message']

		user = User.objects.first()  # TODO: get the currently logged in user

		topic = Topic.objects.create(
			subject=subject,
			forum=forums,
			started_by=user
			)

		post = Post.objects.create(
			message=message,
			topic=topic,
			created_by=user
			)

		return redirect('forum_topics', pk=forums.pk)  # TODO: redirect to the created topic page

	return render(request,'new_topics.html',{'forums':forums})
