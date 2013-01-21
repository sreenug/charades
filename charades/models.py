from django.db import models

# Create your models here.
class User(models.Model):
    fuid = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    coins = models.IntegerField()
    
    class Meta:
        db_table = 'user'

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'category'
		
class Video(models.Model):
    tokbox_id = models.IntegerField()
    category = models.ForeignKey(Category)
    
    class Meta:
        db_table = 'video'
		
class UserChallanges(models.Model):
    user_fuid = models.IntegerField()
    friend_fuid = models.IntegerField()
    video_id = models.ForeignKey(Video)
    status = models.CharField(max_length=1)
    
    class Meta:
        db_table = 'user_challanges'
