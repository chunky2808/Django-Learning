from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from .forms import NewTopicForm
from .models import Forum,Topic,Post


def home(request):
	forums = Forum.objects.all()
	return render(request,'home.html',{'forums' : forums})

def forum_topics(request,pk):
	forums = get_object_or_404(Forum, pk=pk)
	return render(request,'topics.html',{'forums': forums})

def new_topic(request, pk):
	forums = get_object_or_404(Forum, pk=pk)
	user = User.objects.first()  # TODO: get the currently logged in user
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.forum = forums
			topic.started_by = user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=user
			)
			return redirect('forum_topics', pk=forums.pk)  # TODO: redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'new_topics.html', {'forums': forums, 'form': form})