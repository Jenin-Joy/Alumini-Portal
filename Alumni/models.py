from django.db import models
from Guest.models import *
from Company.models import *
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_replay=models.CharField(max_length=50)
    alumni=models.ForeignKey(tbl_alumni,on_delete=models.CASCADE)
    

class tbl_request(models.Model):
    request_date = models.DateField(auto_now_add=True)
    workshop = models.ForeignKey(tbl_workshop, on_delete=models.CASCADE, null=True)
    jobpost = models.ForeignKey(tbl_jobpost, on_delete=models.CASCADE, null=True)
    internship = models.ForeignKey(tbl_internship, on_delete=models.CASCADE, null=True)
    alumni = models.ForeignKey(tbl_alumni, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(tbl_student, on_delete=models.CASCADE, null=True)
    request_status=models.IntegerField(default=0)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    alumni=models.ForeignKey(tbl_alumni,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

class tbl_payment(models.Model):
    alumin = models.ForeignKey(tbl_alumni, on_delete= models.CASCADE)
    amount = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)

class tbl_achivements(models.Model):
    achivement_title=models.CharField(max_length=50)
    achivement_description=models.CharField(max_length=50)
    achivement_photo = models.FileField(upload_to='Assets/achivements/photo')
    alumni=models.ForeignKey(tbl_alumni,on_delete=models.CASCADE)