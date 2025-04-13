from django.db import models
from Guest.models import *

class tbl_workshop(models.Model):
    workshop_name=models.CharField(max_length=50)
    workshop_description=models.CharField(max_length=50)
    workshop_photo=models.FileField(upload_to='assets/workshop/photo')
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)

class tbl_jobpost(models.Model):
    job_title=models.CharField(max_length=50)
    job_description=models.CharField(max_length=50)
    job_date = models.DateField(auto_now_add=True)
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)

class tbl_internship(models.Model):
    internship_title=models.CharField(max_length=50)
    internship_description=models.CharField(max_length=50)
    internship_date = models.DateField(auto_now_add=True)
    internship_photo=models.FileField(upload_to='Assets/internship/photo')
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)