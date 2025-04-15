from django.urls import path,include
from Admin.models import *
from Student import views

app_name="Student"
urlpatterns = [
path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('Viewjobpost/',views.Viewjobpost,name="Viewjobpost"),
    path('requestjob/<int:id>',views.requestjob,name="requestjob"),
    path('Viewinternship/',views.Viewinternship,name="Viewinternship"),
    path('requestinternship/<int:id>',views.requestinternship,name="requestinternship"),
    path('MyRequest/',views.MyRequest,name="MyRequest"),

    path('ViewAlumini/',views.ViewAlumini,name="ViewAlumini"),
    path('friendrequest/<int:id>',views.friendrequest,name="friendrequest"),
    path('My_friends/',views.My_friends,name="My_friends"),
    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
]
