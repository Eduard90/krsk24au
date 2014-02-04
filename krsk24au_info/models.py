from django.db import models
from djangosphinx.models import SphinxSearch
from django.contrib import admin


# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    uniq = models.CharField(max_length=40)
    good_id = models.IntegerField()
    user = models.ForeignKey('User')
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    search = SphinxSearch(
        index='review',
        weights={
            'title': 100,
        },
    )
    user_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-date_time']
    #     managed = False
    #     db_table = 'review'


    def __unicode__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    #class Meta:
    #     managed = False
    #     db_table = 'user'

    def __unicode__(self):
        return self.name