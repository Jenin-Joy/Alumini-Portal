from django.shortcuts import render,redirect
from Admin.models import *
from Student.models import *
def home(request):
        return render(request,'Student/Homepage.html',{'home':home})

def profile(request):
        student=tbl_student.objects.get(id=request.session["sid"])
        return render(request,'Student/profile.html',{'student':student})

def EditProfile(request):
     b=tbl_student.objects.get(id=request.session["sid"])
     if request.method=="POST":
        b.student_name=request.POST.get("name")
        b.student_email=request.POST.get("email")
        b.student_contact=request.POST.get("contact")
        b.student_address=request.POST.get("address")
        b.save()
        return redirect("Student:profile")
     else:
         return render(request,"Student/EditProfile.html",{'student':b})

def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_student.objects.get(id=request.session['sid'])
     olda=b.student_password
     oldb= new=request.POST.get("txt_oldpassword")
     new=request.POST.get("txt_newpassword")
     re=request.POST.get("txt_retypepassword")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.student_password=request.POST.get("txt_retypepassword")
                b.save()
                return redirect("Student:profile")
            else:
                return render(request,"Student/ChangePassword.html",{'error1':error1})
        else:
            return render(request,"Student/ChangePassword.html",{'error2':error2})
     else:
         return render(request,"Student/ChangePassword.html")