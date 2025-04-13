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

def Viewjobpost(request):
    job=tbl_jobpost.objects.all()
    return render(request,'User/ViewJobpost.html',{'job':job})

def requestjob(request,id):
    jobcount = tbl_request.objects.filter(jobpost=id,user=request.session["uid"]).count()
    if jobcount > 0:
        return render(request,"User/ViewJobpost.html",{"msg":"Request Already Send..."})
    tbl_request.objects.create(jobpost=tbl_jobpost.objects.get(id=id),user=tbl_user.objects.get(id=request.session["uid"]))
    return render(request,"User/ViewJobpost.html",{"msg":"Request Send Sucessfully..."})

def Viewinternship(request):
    internship=tbl_internship.objects.all()
    return render(request,'User/ViewInternship.html',{'internship':internship})

def requestinternship(request,id):
    internshipcount = tbl_request.objects.filter(internship=id,user=request.session["uid"]).count()
    if internshipcount > 0:
        return render(request,"User/ViewInternship.html",{"msg":"Request Already Send..."})    
    tbl_request.objects.create(internship=tbl_internship.objects.get(id=id),user=tbl_user.objects.get(id=request.session["uid"]))    
    return render(request,"User/ViewInternship.html",{"msg":"Request Send Sucessfully..."})    

def MyRequest(request):
    jobrequest=tbl_request.objects.filter(user=request.session["uid"],jobpost__isnull=False)
    internshiprequest=tbl_request.objects.filter(user=request.session["uid"],internship__isnull=False)
    return render(request,"User/MyRequest.html",{"jobrequest":jobrequest,"internshiprequest":internshiprequest})

def ViewAlumini(request):
    alu=tbl_alumni.objects.all()
    return render(request,"User/ViewAlumini.html",{"alumini":alu})

def friendrequest(request,id):
    friendcount = tbl_friend_request.objects.filter(alumini=id,user=request.session["uid"]).count()
    if friendcount > 0:
        return render(request,"User/ViewAlumini.html",{"msg":"Request Already Send..."})
    tbl_friend_request.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),alumini=tbl_alumni.objects.get(id=id))
    return render(request,"User/ViewAlumini.html",{"msg":"Request Send Sucessfully..."})

def My_friends(request):
    friend = tbl_friend_request.objects.filter(user=request.session["uid"],request_status=1)
    return render(request,"User/My_friends.html",{"friend":friend})

def chatpage(request,id):
    user  = tbl_alumni.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_alumni = tbl_alumni.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,alumni_to=to_alumni,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(alumni_from=tid) | Q(alumni_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(alumni_to=request.GET.get("tid")) | (Q(alumni_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})