from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from Alumni.models import *
from Company.models import *
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime


def home(request):
        return render(request,'Alumni/Homepage.html',{'home':home})

def profile(request):
        alumni=tbl_alumni.objects.get(id=request.session["alid"])
        return render(request,'Alumni/Myprofile.html',{'alumni':alumni})

def EditProfile(request):
     b=tbl_alumni.objects.get(id=request.session["alid"])
     if request.method=="POST":
        b.alumni_name=request.POST.get("name")
        b.alumni_email=request.POST.get("email")
        b.alumni_contact=request.POST.get("contact")
        b.alumni_address=request.POST.get("address")
        b.save()
        return redirect("Alumni:profile")
     else:
         return render(request,"Alumni/EditProfile.html",{'alumni':b})

def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_alumni.objects.get(id=request.session['alid'])
     olda=b.alumni_password
     oldb= new=request.POST.get("txt_oldpassword")
     new=request.POST.get("txt_newpassword")
     re=request.POST.get("txt_retypepassword")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.alumni_password=request.POST.get("txt_retypepassword")
                b.save()
                return redirect("Alumni:Myprofile")
            else:
                return render(request,"Alumni/ChangePassword.html",{'error1':error1})
        else:
            return render(request,"Alumni/ChangePassword.html",{'error2':error2})
     else:
         return render(request,"Alumni/ChangePassword.html")

def Viewcompany(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    company=tbl_company.objects.filter(company_status=1)
    for i in company:
        tot=0
        ratecount=tbl_rating.objects.filter(company=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(company=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(company,parry)
    return render(request,'Alumni/Viewcompany.html',{'company':datas,"ar":ar})

def Viewworkshop(request, id): 
    workshop = tbl_workshop.objects.filter(company=id)
    return render(request,'Alumni/Viewworkshop.html',{"workshop":workshop})

def Feedback(request): 
    return render(request,'Alumni/Feedback.html')


def Complaint(request):
    b=tbl_complaint.objects.all()
    if request.method=="POST":
       tbl_complaint.objects.create(complaint_title=request.POST.get("title"),complaint_content=request.POST.get("content"),
        alumni=tbl_alumni.objects.get(id=request.session['alid']))
   
       return redirect("Alumni:Complaint")
       
    else:
        return render(request,"Alumni/Complaint.html",{'complaint':b})

def requestworkpost(request, id):
    tbl_request.objects.create(workshop=tbl_workshop.objects.get(id=id),alumni=tbl_alumni.objects.get(id=request.session["alid"]))
    return render(request,"Alumni/Viewworkshop.html",{"msg":"Request Send Sucessfully..."})

def viewmyrequest(request):
    req = tbl_request.objects.filter(alumni=request.session["alid"])
    return render(request,"Alumni/View_Myrequest.html",{"workshop":req})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(company=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(company=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"Alumni/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"Alumni/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(alumni=tbl_alumni.objects.get(id=request.session["alid"]),user_review=user_review,rating_data=rating_data,company=tbl_company.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(company=pid).order_by('-datetime')
    return render(request,"Alumni/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(company=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(company=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def Viewnotification(request):
    noti = tbl_notification.objects.all()  
    if request.method == "POST":
        notification = request.POST.get('Notification')  
        tbl_notification.objects.create(notification_content=notification)  
        return render(request, 'Alumni/Viewnotification.html', {'notification': noti})  
    else:
        return render(request, 'Alumni/Viewnotification.html', {'notification': noti})  

def sponser(request):
    if request.method == "POST":
        tbl_payment.objects.create(
            alumin = tbl_alumni.objects.get(id=request.session["alid"]),
            amount = request.POST.get("txt_amount"),
        )
        return redirect("Alumni:loader")
    return render(request,"Alumni/Payment.html")

def loader(request):
    return render(request,"Alumni/Loader.html")

def paymentsuc(request):
    return render(request,"Alumni/Paymentsuc.html")

def delcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("Alumni:Complaint")

def Achivements(request):
    achivements = tbl_achivements.objects.filter(alumni=request.session["alid"])
    if request.method == "POST":
        tbl_achivements.objects.create(
            achivement_title = request.POST.get("achivement_title"),
            achivement_description = request.POST.get("achivement_description"),
            achivement_photo = request.FILES.get("achivement_photo"),
            alumni = tbl_alumni.objects.get(id=request.session["alid"])
        )
        return redirect("Alumni:Achivements")
    return render(request,"Alumni/Achivements.html",{"achivements":achivements})

def delachivement(request,id):
    tbl_achivements.objects.get(id=id).delete()
    return redirect("Alumni:Achivements")

def ViewFriend_request(request):
    friend = tbl_friend_request.objects.filter(alumini=request.session["alid"])
    return render(request,"Alumni/ViewFriend_request.html",{"friend":friend})

def acceptfriendrequest(request,id):
    friend = tbl_friend_request.objects.get(id=id)
    friend.request_status = 1
    friend.save()
    return redirect("Alumni:ViewFriend_request")

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Alumni/Chat.html",{"user":user})

def ajaxchat(request):
    from_alumni = tbl_alumni.objects.get(id=request.session["alid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),alumni_from=from_alumni,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Alumni/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    alumni = tbl_alumni.objects.get(id=request.session["alid"])
    chat_data = tbl_chat.objects.filter((Q(alumni_from=alumni) | Q(alumni_to=alumni)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Alumni/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(alumni_from=request.session["alid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(alumni_to=request.session["alid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})