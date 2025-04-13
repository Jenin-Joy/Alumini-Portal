from django.urls import path,include
from Admin import views

app_name="Admin"

urlpatterns = [
  path('add/',views.add,name='add'),  
  # path('largest/',views.Largest,name='largest'),  
  path('district/',views.district,name='district'),  
  path('category/',views.category,name='category'),
  path('adminreg/',views.adminreg,name='adminreg'),
  path('deladmin/<int:id>',views.deladmin,name='deladmin'),
  path('deldistrict/<int:id>',views.deldistrict,name='deldistrict'),
  path('place/',views.place,name='place'),
  path('delplace/<int:id>',views.delplace,name='delplace'),
  path('editplace/<int:id>',views.editplace,name='editplace'),
  path('subcategory/',views.subcategory,name='subcategory'),
  path('delsubcategory/<int:id>',views.delsubcategory,name='delsubcategory'),
  path('editsub/<int:id>',views.editsub,name='editsub'),
  path('batch/',views.batch,name='batch'),
  path('Viewalumni/',views.Viewalumni,name="Viewalumni"),
  path('homepage/',views.homepage,name="homepage"),
  path('alumniaccept/<int:id>',views.alumniaccept,name="alumniaccept"),
  path('alumnireject/<int:id>',views.alumnireject,name="alumnireject"),
  path('acceptedalumni/',views.acceptedalumni,name="acceptedalumni"),
  path('rejectedalumni/',views.rejectedalumni,name="rejectedalumni"),

path('Viewcompany/',views.Viewcompany,name="Viewcompany"),
  path('companyaccept/<int:id>',views.companyaccept,name="companyaccept"),
  path('companyreject/<int:id>',views.companyreject,name="companyreject"),
  path('acceptedcompany/',views.acceptedcompany,name="acceptedcompany"),
  path('rejectedalumni/',views.rejectedcompany,name="rejectedcompany"),
  #path('reply/',views.reply,name="reply"),  
  path('repliedcomplaints/',views.repliedcomplaints,name="repliedcomplaints"),
  path('Viewcomplaint/',views.Viewcomplaint,name="Viewcomplaint1"),
  path('Viewfeedback/',views.Viewfeedback,name="Viewfeedback"),
  path('Notification/',views.notification,name="Notification"),
  path('delnotification/<int:id>',views.delnotification,name='delnotification'),
  path('delbatch/<int:id>',views.delbatch,name='delbatch'),
  path('StudentReg/',views.StudentReg,name='StudentReg'),
  path('studentdelete/',views.studentdelete,name="studentdelete"),
]

