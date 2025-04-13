from django.urls import path, include
from Guest import views
app_name="Guest"

urlpatterns=[
    path('login/',views.login,name='login'),
    path('Registration/',views.Registration,name='Registration'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('login/',views.login,name='login'),
    path('AlumniReg/',views.AlumniReg,name='AlumniReg'),
    path('CompanyReg/',views.CompanyReg,name='CompanyReg'),
    path('',views.index,name='index'),
    
    


]

