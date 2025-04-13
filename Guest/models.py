from django.db import models
from Admin.models import *
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to='Assets/user/photo/')
    user_password=models.CharField(max_length=50)

class tbl_alumni(models.Model):
    alumni_name=models.CharField(max_length=50)
    alumni_email=models.CharField(max_length=50)
    alumni_contact=models.CharField(max_length=50)
    alumni_address=models.CharField(max_length=50)
    alumni_password=models.CharField(max_length=50)
    alumni_photo=models.FileField(upload_to='assets/alumni/photo')
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE)
    alumni_status=models.IntegerField(default=0)

class tbl_company(models.Model):
    company_name=models.CharField(max_length=50)
    company_email=models.CharField(max_length=50)
    company_contact=models.CharField(max_length=50)
    company_address=models.CharField(max_length=50)
    company_password=models.CharField(max_length=50)
    company_photo=models.FileField(upload_to='assets/company/photo')
    company_logo=models.FileField(upload_to='assets/company/logo')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    company_status=models.IntegerField(default=0)
    



