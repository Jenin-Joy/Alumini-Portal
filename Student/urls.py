from django.urls import path,include
from Admin.models import *
from Student import views

app_name="Student"
urlpatterns = [
path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
]
