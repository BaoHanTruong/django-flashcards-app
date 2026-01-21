import random
from django.shortcuts import render, get_object_or_404
from .models import Topic

# Home View
def home(request):
    topics = Topic.objects.all()
    return render(request, 'home.html', {'topics': topics})

def flashcards(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    words = list(topic.words.all())
    random.shuffle(words)  # Xáo trộn danh sách từ vựng mỗi lần tải trang
    return render(request, 'flashcards.html', {'topic': topic, 'words': words})