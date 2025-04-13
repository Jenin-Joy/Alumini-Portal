from django.shortcuts import render,redirect

from Guest.models import *
from Admin.models import *
from Student.models import *
# Create your views here.
def Registration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
       
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("file_photo")
        tbl_user.objects.create(user_name=name,user_email=email,user_address=address,user_contact=contact,user_password=password,place=place,user_photo=photo)
    return render(request,'Guest/Registration.html',{'result':dis})
    #else:
    #   return render(request,'Guest/Registration.html')
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})


def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        alumnicount=tbl_alumni.objects.filter(alumni_email=email,alumni_password=password).count()
        studentcount=tbl_student.objects.filter(student_email=email,student_password=password).count()
        admincount=tbl_adminreg.objects.filter(adminreg_email=email,adminreg_password=password).count()
        companycount=tbl_company.objects.filter(company_email=email,company_password=password).count()
        if usercount > 0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect("User:home")
        elif alumnicount > 0:
            alumni=tbl_alumni.objects.get(alumni_email=email,alumni_password=password)
            request.session["alid"]=alumni.id
            return redirect("Alumni:home")
        
        elif studentcount > 0:
            student=tbl_student.objects.get(student_email=email,student_password=password)
            request.session["sid"]=student.id
            return redirect("Student:home")

        elif admincount > 0:
            admin=tbl_adminreg.objects.get(adminreg_email=email,adminreg_password=password)
            request.session["aid"]=admin.id
            return redirect("Admin:homepage")
        elif companycount > 0:
            company=tbl_company.objects.get(company_email=email,company_password=password)
            request.session["cid"]=company.id
            return redirect("Company:homepage")
        else:
            return render(request,'Guest/Login.html')
    else:
        return render(request,'Guest/Login.html') 

def AlumniReg(request):
    bat=tbl_batch.objects.all()
    if request.method=="POST":
        batch=tbl_batch.objects.get(id=request.POST.get("Batchid"))
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
        photo=request.FILES.get("file_photo")
        tbl_alumni.objects.create(alumni_name=name,alumni_email=email,alumni_address=address,alumni_contact=contact,alumni_password=password,alumni_photo=photo,batch=batch)
        return render(request,'Guest/AlumniReg.html',{'batch': bat})
    else:
        return render(request,'Guest/AlumniReg.html',{'batch': bat})  

def CompanyReg(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
       
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("file_photo")
        logo=request.FILES.get("file_logo")
        tbl_company.objects.create(company_name=name,company_email=email,company_address=address,company_contact=contact,company_password=password,place=place,company_photo=photo,company_logo=logo)
    return render(request,'Guest/CompanyReg.html',{'result':dis})

def index(request):
    return render(request,'Guest/index.html')