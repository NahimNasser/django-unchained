from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=50)
    pub_date = models.DateTimeField()


class Choice(models.Model):

    poll = models.ForeignKey(Poll)
    choice= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


