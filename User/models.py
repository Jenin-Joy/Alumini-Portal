from django.db import models
from Guest.models import *
# Create your models here.

class tbl_friend_request(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    alumini = models.ForeignKey(tbl_alumni, on_delete=models.CASCADE)
    request_status = models.IntegerField(default=0)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    alumni_from = models.ForeignKey(tbl_alumni,on_delete=models.CASCADE,related_name="alumni_from",null=True)
    alumni_to = models.ForeignKey(tbl_alumni,on_delete=models.CASCADE,related_name="alumni_to",null=True)