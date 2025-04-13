from django.shortcuts import render,redirect
from Company.models import *
from Alumni.models import *

def homepage(request):
    return render(request,'Company/Homepage.html')

def Workshop(request):
    wor=tbl_workshop.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        photo=request.FILES.get("file_photo")
        companyid=tbl_company.objects.get(id=request.session['cid'])
        tbl_workshop.objects.create(company=companyid,workshop_name=name,workshop_description=description,workshop_photo=photo)
        return render(request,'Company/Workshop.html',{'work':wor})
    else:
        return render(request,'Company/Workshop.html',{'work':wor})

def Viewrequest(request,id):
    rq=tbl_request.objects.filter(workshop=id)
    return render(request,'Company/Viewrequest.html',{'result':rq, "id":id})

def requestaccept(request,id, work):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=1
    rq.save()
    return redirect("Company:Viewrequest",work)

def requestreject(request,id, work):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=2
    rq.save()
    return redirect("Company:Viewrequest",work)

def profile(request):
    company=tbl_company.objects.get(id=request.session["cid"])
    return render(request,'Company/Profile.html',{'company':company})

def EditProfile(request):
     b=tbl_company.objects.get(id=request.session["cid"])
     if request.method=="POST":
        b.company_name=request.POST.get("name")
        b.company_email=request.POST.get("email")
        b.company_contact=request.POST.get("contact")
        b.company_address=request.POST.get("address")
        b.save()
        return redirect("Company:Profile")
     else:
         return render(request,"Company/EditProfile.html",{'company':b})

def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_company.objects.get(id=request.session['cid'])
     olda=b.company_password
     oldb= new=request.POST.get("txt_oldpassword")
     new=request.POST.get("txt_newpassword")
     re=request.POST.get("txt_retypepassword")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.company_password=request.POST.get("txt_retypepassword")
                b.save()
                return redirect("Company:Profile")
            else:
                return render(request,"Company/ChangePassword.html",{'error1':error1})
        else:
            return render(request,"Company/ChangePassword.html",{'error2':error2})
     else:
         return render(request,"Company/ChangePassword.html")

def Job_Post(request):
    job=tbl_jobpost.objects.filter(company=request.session['cid'])
    if request.method=="POST":
        name=request.POST.get("job_title")
        description=request.POST.get("job_description")
        companyid=tbl_company.objects.get(id=request.session['cid'])
        tbl_jobpost.objects.create(company=companyid,job_title=name,job_description=description)
        return redirect("Company:Job_Post")
    else:
        return render(request,'Company/Job_Post.html',{'job':job})

def Viewjobrequest(request,id):
    rq=tbl_request.objects.filter(jobpost=id)
    return render(request,'Company/Viewjobrequest.html',{'result':rq, "id":id})

def requestjobaccept(request,id, jobid):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=1
    rq.save()
    return redirect("Company:Viewjobrequest",jobid)

def requestjobreject(request,id, jobid):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=2
    rq.save()
    return redirect("Company:Viewjobrequest",jobid)

def deljob(request,id):
    tbl_jobpost.objects.get(id=id).delete()
    return redirect("Company:Job_Post")

def editjob(request,id):
    b=tbl_jobpost.objects.get(id=id)
    if request.method=="POST":
        b.job_title=request.POST.get("job_title")
        b.job_description=request.POST.get("job_description")
        b.save()
        return redirect("Company:Job_Post")
    else:
        return render(request,"Company/Job_Post.html",{'editjob':b})

def Internship(request):
    internship=tbl_internship.objects.filter(company=request.session['cid'])
    if request.method=="POST":
        name=request.POST.get("internship_title")
        description=request.POST.get("internship_description")
        photo=request.FILES.get("internship_photo")
        companyid=tbl_company.objects.get(id=request.session['cid'])
        tbl_internship.objects.create(company=companyid,internship_title=name,internship_description=description,internship_photo=photo)
        return redirect("Company:Internship")
    else:
        return render(request,'Company/Internship.html',{'internship':internship})

def Viewinternshiprequest(request,id):
    rq=tbl_request.objects.filter(internship=id)
    return render(request,'Company/Viewinternshiprequest.html',{'result':rq, "id":id})

def requestinternshipaccept(request,id, internshipid):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=1
    rq.save()
    return redirect("Company:Viewinternshiprequest",internshipid)

def requestinternshipreject(request,id, internshipid):
    rq=tbl_request.objects.get(id=id)
    rq.request_status=2
    rq.save()
    return redirect("Company:Viewinternshiprequest",internshipid)

def delinternship(request,id):
    tbl_internship.objects.get(id=id).delete()
    return redirect("Company:Internship")