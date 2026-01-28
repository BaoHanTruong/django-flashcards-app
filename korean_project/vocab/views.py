import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Vocabulary

# Home view
def home(request):
    topics = Topic.objects.all()
    return render(request, 'home.html', {'topics': topics})

# Flashcards view
def flashcards(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    words = Vocabulary.objects.filter(topic=topic).order_by('id')
    total = words.count()
    
    index = int(request.GET.get('index', 0))
    
    if index < 0: 
        index = 0
    if index >= total and total > 0: 
        index = total - 1

    word = words[index] if total > 0 else None
    
    if total > 0:
        progress = ((index + 1) / total) * 100
    else:
        progress = 0

    return render(request, 'flashcards.html', {
        'topic': topic,
        'word': word,
        'index': index,
        'total': total,
        'prev_index': index - 1,
        'next_index': index + 1,
        'progress': progress,
    })