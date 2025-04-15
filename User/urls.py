from django.urls import path,include
from User import views

app_name="User"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/<int:id>',views.ChangePassword,name='ChangePassword'),
]