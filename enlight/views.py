from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404
from .forms import NewTopicForm,PostForm
from .models import Forum,Topic,Post


def home(request):
	forums = Forum.objects.all()
	return render(request,'home.html',{'forums' : forums})

def forum_topics(request,pk):
	forums = get_object_or_404(Forum, pk=pk)
	topics = forums.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
	for topic in topics:
		print(topic.replies)
	return render(request,'topics.html',{'forums': forums,'topics': topics})

@login_required
def new_topic(request, pk):
	forums = get_object_or_404(Forum, pk=pk)
	user = User.objects.first()  # TODO: get the currently logged in user
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.forum = forums
			topic.started_by = request.user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=request.user
			)
			#print(post.pk)
			return redirect('forum_topics', pk=pk, topic_pk=topic.pk)  # TODO: redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'new_topics.html', {'forums': forums, 'form': form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, forum__pk=pk, pk=topic_pk)
    return render(request, 'topic_post.html', {'topic': topic})	

@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, forum__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})    