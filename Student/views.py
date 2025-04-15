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

def Viewjobpost(request):
    job=tbl_jobpost.objects.all()
    return render(request,'Student/ViewJobpost.html',{'job':job})

def requestjob(request,id):
    jobcount = tbl_request.objects.filter(jobpost=id,student=request.session["sid"]).count()
    if jobcount > 0:
        return render(request,"Student/ViewJobpost.html",{"msg":"Request Already Send..."})
    tbl_request.objects.create(jobpost=tbl_jobpost.objects.get(id=id),student=tbl_student.objects.get(id=request.session["sid"]))
    return render(request,"Student/ViewJobpost.html",{"msg":"Request Send Sucessfully..."})

def Viewinternship(request):
    internship=tbl_internship.objects.all()
    return render(request,'Student/ViewInternship.html',{'internship':internship})

def requestinternship(request,id):
    internshipcount = tbl_request.objects.filter(internship=id,student=request.session["sid"]).count()
    if internshipcount > 0:
        return render(request,"Student/ViewInternship.html",{"msg":"Request Already Send..."})    
    tbl_request.objects.create(internship=tbl_internship.objects.get(id=id),student=tbl_student.objects.get(id=request.session["sid"]))    
    return render(request,"Student/ViewInternship.html",{"msg":"Request Send Sucessfully..."})    

def MyRequest(request):
    jobrequest=tbl_request.objects.filter(student=request.session["sid"],jobpost__isnull=False)
    internshiprequest=tbl_request.objects.filter(student=request.session["sid"],internship__isnull=False)
    return render(request,"Student/MyRequest.html",{"jobrequest":jobrequest,"internshiprequest":internshiprequest})

def ViewAlumini(request):
    alu=tbl_alumni.objects.all()
    return render(request,"Student/ViewAlumini.html",{"alumini":alu})

def friendrequest(request,id):
    friendcount = tbl_friend_request.objects.filter(alumini=id,student=request.session["sid"]).count()
    if friendcount > 0:
        return render(request,"Student/ViewAlumini.html",{"msg":"Request Already Send..."})
    tbl_friend_request.objects.create(student=tbl_student.objects.get(id=request.session["sid"]),alumini=tbl_alumni.objects.get(id=id))
    return render(request,"Student/ViewAlumini.html",{"msg":"Request Send Sucessfully..."})

def My_friends(request):
    friend = tbl_friend_request.objects.filter(student=request.session["sid"],request_status=1)
    return render(request,"Student/My_friends.html",{"friend":friend})

def chatpage(request,id):
    student  = tbl_alumni.objects.get(id=id)
    return render(request,"Student/Chat.html",{"student":student})

def ajaxchat(request):
    from_student = tbl_student.objects.get(id=request.session["sid"])
    to_alumni = tbl_alumni.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),student_from=from_student,alumni_to=to_alumni,chat_file=request.FILES.get("file"))
    return render(request,"Student/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    student = tbl_student.objects.get(id=request.session["sid"])
    chat_data = tbl_chat.objects.filter((Q(student_from=student) | Q(student_to=student)) & (Q(alumni_from=tid) | Q(alumni_to=tid))).order_by('chat_time')
    return render(request,"Student/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(student_from=request.session["sid"]) & Q(alumni_to=request.GET.get("tid")) | (Q(alumni_from=request.GET.get("tid")) & Q(student_to=request.session["sid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})