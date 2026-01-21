from django.db import models

# Models
class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên chủ đề")
    def __str__(self):
        return self.name

class Vocabulary(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=100, verbose_name="Từ tiếng Hàn")
    meaning = models.CharField(max_length=200, verbose_name="Nghĩa tiếng Việt")
    example = models.TextField(blank=True, verbose_name="Ví dụ")

    def __str__(self):
        return self.word