from django.urls import path,include
from Alumni import views

app_name="Alumni"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    
    path('Viewcompany/',views.Viewcompany,name="Viewcompany"),
    path('Viewworkshop/<int:id>',views.Viewworkshop,name="Viewworkshop"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('requestworkpost/<int:id>',views.requestworkpost,name="requestworkpost"),
    path('viewmyrequest/',views.viewmyrequest,name="viewmyrequest"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path('viewnotification/',views.Viewnotification,name="viewnotification"),

    path('sponser/',views.sponser,name="sponser"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path('delcomplaint/<int:id>',views.delcomplaint,name='delcomplaint'),

    path('Achivements/',views.Achivements,name="Achivements"),
    path('delachivement/<int:id>',views.delachivement,name="delachivement"),

    path('ViewFriend_request/',views.ViewFriend_request,name="ViewFriend_request"),
    path('acceptfriendrequest/<int:id>',views.acceptfriendrequest,name="acceptfriendrequest"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    

]