from django.db import models
from Guest.models import *

# Create your models here.

class tbl_friend_request(models.Model):
    student = models.ForeignKey(tbl_student, on_delete=models.CASCADE)
    alumini = models.ForeignKey(tbl_alumni, on_delete=models.CASCADE)
    request_status = models.IntegerField(default=0)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    student_from = models.ForeignKey(tbl_student,on_delete=models.CASCADE,related_name="student_from",null=True)
    student_to = models.ForeignKey(tbl_student,on_delete=models.CASCADE,related_name="student_to",null=True)
    alumni_from = models.ForeignKey(tbl_alumni,on_delete=models.CASCADE,related_name="alumni_from",null=True)
    alumni_to = models.ForeignKey(tbl_alumni,on_delete=models.CASCADE,related_name="alumni_to",null=True)