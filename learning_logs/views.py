from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show topic and related entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted create a blank form
        form = TopicForm()
    else:
        # Data submitted; process
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry related to the topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted - create a blank form
        form = EntryForm()
    else:
        # Data submitted; process
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edits an already existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # No data submitted - create a blank form, fill with previous value
        form = EntryForm()
    else:
        # Data submitted; process
        form = EntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
