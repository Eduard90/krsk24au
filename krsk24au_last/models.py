from django.db import models

# Create your models here.
class NewReview(models.Model):
    id = models.AutoField(primary_key=True)
    uniq = models.CharField(max_length=32)
    good_id = models.IntegerField()
    seller = models.ForeignKey('NewUser', related_name='seller')
    buyer = models.ForeignKey('NewUser', related_name='buyer')
    title = models.CharField(max_length=250)
    review_id = models.IntegerField()
    review_link = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    seller_user_name = models.CharField(max_length=50)
    buyer_user_name = models.CharField(max_length=50)

    # class Meta:
        # ordering = ['-date_time']
    #     managed = False
    #     db_table = 'review'


    def __unicode__(self):
        return self.title

class NewUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    #class Meta:
    #     managed = False
    #     db_table = 'user'

    def __unicode__(self):
        return self.name