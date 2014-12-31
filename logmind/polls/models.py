import datetime
from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def date_posted_by(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    date_posted_by.admin_order_field = 'pub_date'
    date_posted_by.boolean = True
    date_posted_by.short_description = 'published_recently'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
# Create your models here.
