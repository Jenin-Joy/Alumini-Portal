from django.urls import path, include
from Company import views
app_name="Company"

urlpatterns=[
    path('Homepage/',views.homepage,name='homepage'),

    path('Workshop/',views.Workshop,name='Workshop'),
    path('Viewrequest/<int:id>',views.Viewrequest,name="Viewrequest"),
    path('requestaccept/<int:id>/<int:work>',views.requestaccept,name="requestaccept"),
    path('requestreject/<int:id>/<int:work>',views.requestreject,name="requestreject"),
    path('Profile/',views.profile,name='Profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),

    path('Job_Post/',views.Job_Post,name='Job_Post'),
    path('Viewjobrequest/<int:id>',views.Viewjobrequest,name="Viewjobrequest"),
    path('requestjobaccept/<int:id>/<int:jobid>',views.requestjobaccept,name="requestjobaccept"),
    path('requestjobreject/<int:id>/<int:jobid>',views.requestjobreject,name="requestjobreject"),
    path('deljob/<int:id>',views.deljob,name="deljob"),
    path('editjob/<int:id>',views.editjob,name="editjob"),

    path('Internship/',views.Internship,name='Internship'),
    path('Viewinternshiprequest/<int:id>',views.Viewinternshiprequest,name="Viewinternshiprequest"),
    path('requestinternshipaccept/<int:id>/<int:internshipid>',views.requestinternshipaccept,name="requestinternshipaccept"),
    path('requestinternshipreject/<int:id>/<int:internshipid>',views.requestinternshipreject,name="requestinternshipreject"),
    path('delinternship/<int:id>',views.delinternship,name="delinternship"),
    
]