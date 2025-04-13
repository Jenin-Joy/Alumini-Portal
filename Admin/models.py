from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
    
class tbl_place(models.Model):
    place_name = models.CharField(max_length=30)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_adminreg(models.Model):
    adminreg_name=models.CharField(max_length=50)
    adminreg_email=models.CharField(max_length=50)
    adminreg_password=models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_batch(models.Model):
    batch_name = models.CharField(max_length=100)

class tbl_notification(models.Model):
    notification_content=models.CharField(max_length=50)
    notification_date=models.CharField(max_length=50)

class tbl_student(models.Model):
    student_name=models.CharField(max_length=50)
    student_email=models.CharField(max_length=50)
    student_contact=models.CharField(max_length=50)
    student_address=models.CharField(max_length=50)
    student_password=models.CharField(max_length=50)
    student_photo=models.FileField(upload_to='assets/admin/photo')
    batch=models.ForeignKey(tbl_batch,on_delete=models.CASCADE)
    student_status=models.IntegerField(default=0)

    





