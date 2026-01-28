import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Vocabulary

# View trang chủ: Hiển thị danh sách các chủ đề (10 bài)
def home(request):
    topics = Topic.objects.all()
    return render(request, 'home.html', {'topics': topics})

# View học tập: Hiển thị các thẻ flashcard theo chủ đề đã chọn
def flashcards(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    words = Vocabulary.objects.filter(topic=topic).order_by('id')
    total = words.count()
    
    # Lấy index hiện tại từ URL
    index = int(request.GET.get('index', 0))
    
    # CHẶN LỖI: Luôn giữ index trong phạm vi từ 0 đến total-1
    if index < 0: 
        index = 0
    if index >= total and total > 0: 
        index = total - 1

    word = words[index] if total > 0 else None
    
    # Tính progress (từ 1 đến total cho dễ nhìn)
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