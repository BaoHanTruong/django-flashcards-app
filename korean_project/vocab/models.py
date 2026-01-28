from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vocabulary(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=255)
    is_learned = models.BooleanField(default=False) 

    def __str__(self):
        return self.word