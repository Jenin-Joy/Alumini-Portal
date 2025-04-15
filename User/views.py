from django.shortcuts import render,redirect
from django.http import JsonResponse
from User.models import *
from Guest.models import *
from Admin.models import *
from Company.models import *
from Alumni.models import *
from datetime import datetime
from django.db.models import Q

def home(request):
        return render(request,'User/Homepage.html',{'home':home})

def profile(request):
        user=tbl_user.objects.get(id=request.session["uid"])
        return render(request,'User/Myprofile.html',{'user':user})

def EditProfile(request):
     b=tbl_user.objects.get(id=request.session["uid"])
     if request.method=="POST":
        b.user_name=request.POST.get("name")
        b.user_email=request.POST.get("email")
        b.user_contact=request.POST.get("contact")
        b.user_address=request.POST.get("address")
        b.save()
        return redirect("User:profile")
     else:
         return render(request,"User/EditProfile.html",{'user':b})

def ChangePassword(request):
        return render(request,'User/changepassword.html')

