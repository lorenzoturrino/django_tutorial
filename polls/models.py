from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text + " | score: " + str(self.votes)
