from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def add(request):
    return render(request,'Admin/Add.html')

def add(request):
    if(request.method=="POST"):
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        c=a+b
        return render(request,"Admin/Add.html",{'result':c})
    else:
            return render(request,"Admin/Add.html")
def Largest(request):
    if(request.method=="POST"):
            a=int(request.POST.get("num1"))
            b=int(request.POST.get("num2"))
            if(a>b):
                return render(request,'Admin/Largest.html',{'result':a})
            else:
                return render(request,'Admin/Largest.html',{'result':b})
    return render(request,'Admin/Largest.html')



def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('district')
        tbl_district.objects.create(district_name=district)
        return render(request,'Admin/District.html',{'dist':dis})
    else:
        return render(request,'Admin/District.html',{'dist':dis})

def category(request):
    cate=tbl_category.objects.all()
    if request.method=="POST":
       category=request.POST.get('category')
       tbl_category.objects.create(category_name=category)
       return render(request,'Admin/Category.html',{'cat':cate})
    else:
        return render(request,'Admin/Category.html',{'cat':cate})   

def adminreg(request):
    result=tbl_adminreg.objects.all()
    if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      password=request.POST.get('password')
      tbl_adminreg.objects.create(adminreg_name=name,adminreg_email=email,adminreg_password=password)
      return render(request,'Admin/AdminReg.html',{'result':result})
    else:
      return render(request,'Admin/AdminReg.html',{'result':result})    

def deladmin(request,id):       
     tbl_adminreg.objects.get(id=id).delete()
     return redirect("Admin:adminreg")  

def deldistrict(request,id):       
     tbl_district.objects.get(id=id).delete()
     return redirect("Admin:district")  
def editdis(request,id):
  district=tbl_district.objects.get(id=id)
  return render(request,'Admin/District.html',{'d':district})

def editdis(request,id):
    district=tbl_district.objects.get(id=id)
    if request.method=="POST":
       district.district_name=request.POST.get("district")
       district.save()
       return redirect("Admin:district")
    else:
        return render(request,'Admin/District.html',{'d':district})


def place(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{'result':dis})
    
def brand(request):
    brand=tbl_brand.objects.all()
    if request.method=="POST":
        brand=request.POST.get("brand")
        tbl_brand.objects.create(brand_name=brand)
        return redirect("Admin:brand")
    else:
        return render(request,'Admin/Brand.html',{'bd':brand})

def delbrand(request,id):
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:brand")

def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")
def editplace(request,id):
    p=tbl_place.objects.get(id=id)
    p1=tbl_place.objects.all()   
    if request.method=="POST":
        p.place_name=request.POST.get("place_name")
        p.save()
        return redirect("Admin:place")
    else:
        return render(request,'Admin/place.html',{'rr':p,'r':p1})

def subcategory(request):
    cat=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        sub=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=request.POST.get("subcategory_name"),category=sub)
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'result':cat,'r':subcategory})
def delsubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")
def editsub(request,id):
    b=tbl_subcategory.objects.get(id=id)
    b1=tbl_category.objects.all()
    if request.method=="POST":
        b.subcategory_name=request.POST.get("subcategory_name")
        b.save()
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'rr':b,'r':b1})

def batch(request):
    bat = tbl_batch.objects.all()  
    if request.method == "POST":
        batch = request.POST.get('Batch')  
        tbl_batch.objects.create(batch_name=batch)  
        return render(request, 'Admin/Batch.html', {'batch': bat})  
    else:
        return render(request, 'Admin/Batch.html', {'batch': bat})  

def delbatch(request,id):
    tbl_batch.objects.get(id=id).delete()
    return redirect("Admin:batch")


def homepage(request): 
    return render(request,'Admin/Homepage.html')

def Viewalumni(request):
    alu=tbl_alumni.objects.filter(alumni_status=0)
    accept=tbl_alumni.objects.filter(alumni_status=1)
    reject=tbl_alumni.objects.filter(alumni_status=2)
    return render(request,'Admin/Viewalumni.html',{'result':alu,'accept':accept,'reject':reject})

def alumniaccept(request,id):
    alu=tbl_alumni.objects.get(id=id)
    alu.alumni_status=1
    alu.save()
    return redirect("Admin:Viewalumni")

def alumnireject(request,id):
    alu=tbl_alumni.objects.get(id=id)
    alu.alumni_status=2
    alu.save()
    return redirect("Admin:Viewalumni")

def acceptedalumni(request):
    alu=tbl_alumni.objects.filter(alumni_status=1)
    if request.method=="POST":
        return render(request,'Admin/Acceptedalumni.html',{'result':alu})
    else:
        return render(request,'Admin/Acceptedalumni.html',{'result':alu})

def rejectedalumni(request):
    alu=tbl_alumni.objects.filter(alumni_status=2)
    if request.method=="POST":
        return render(request,'Admin/Rejectedalumni.html',{'result':alu})
    else:
        return render(request,'Admin/Rejectedalumni.html',{'result':alu})

def Viewcompany(request):
    com=tbl_company.objects.filter(company_status=0)
    accept=tbl_company.objects.filter(company_status=1)
    reject=tbl_company.objects.filter(company_status=2)
    return render(request,'Admin/Viewcompany.html',{'result':com,'accept':accept,'reject':reject})

def companyaccept(request,id):
    com=tbl_company.objects.get(id=id)
    com.company_status=1
    com.save()
    return redirect("Admin:Viewcompany")

def companyreject(request,id):
    com=tbl_company.objects.get(id=id)
    com.company_status=2
    com.save()
    return redirect("Admin:Viewcompany")

def acceptedcompany(request):
    com=tbl_company.objects.filter(company_status=1)
    if request.method=="POST":
        return render(request,'Admin/Acceptedcompany.html',{'result':com})
    else:
        return render(request,'Admin/Acceptedcompany.html',{'result':com})

def rejectedcompany(request):
    com=tbl_company.objects.filter(company_status=2)
    if request.method=="POST":
        return render(request,'Admin/Rejectedcompany.html',{'result':com})
    else:
        return render(request,'Admin/Rejectedcompany.html',{'result':com})

def Viewcomplaint(request): 
    return render(request,'Admin/Viewcomplaint.html')

def Viewfeedback(request): 
    return render(request,'Admin/Viewfeedback.html')

def replay(request,id):
        return render(request,'Admin/replay.html')

def repliedcomplaints(request): 
    return render(request,'Admin/Repliedcomplaint.html')

def notification(request):
    noti = tbl_notification.objects.all()  
    if request.method == "POST":
        notification = request.POST.get('Notification')  
        tbl_notification.objects.create(notification_content=notification)  
        return render(request, 'Admin/Notification.html', {'notification': noti})  
    else:
        return render(request, 'Admin/Notification.html', {'notification': noti})  

def delnotification(request,id):
    tbl_notification.objects.get(id=id).delete()
    return redirect("Admin:Notification")

def StudentReg(request):
    bat=tbl_batch.objects.all()
    if request.method=="POST":
        batch=tbl_batch.objects.get(id=request.POST.get("Batchid"))
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
        photo=request.FILES.get("file_photo")
        tbl_student.objects.create(student_name=name,student_email=email,student_address=address,student_contact=contact,student_password=password,student_photo=photo,batch=batch)
        return render(request,'Admin/StudentReg.html',{'batch': bat})
    else:
        return render(request,'Admin/StudentReg.html',{'batch': bat})  

def studentdelete(request,id):
    tbl_student.objects.get(id=id).delete()
    return redirect("Admin:Viewstudent")




