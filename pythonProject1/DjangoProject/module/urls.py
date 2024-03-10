from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',newhomepage,name='newhomepage'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('contactus/',Contactus,name='contactus'),
    path('logout/',logout,name='logout'),
    path('feedback/',feedback,name='feedback'),
    path('feedbackfunction/',feedbackfunction,name='feedbackfunction'),
    path('Aboutus/',AboutUs,name='Aboutus'),
    path('login_doctor/',login2_doctor,name='login_doctor'),
    path('login_doctor/',login_doctor,name='login_doctor'),
    path('signup_doctor/', signup2_doctor, name='signup_doctor'),
    path('signup_doctor/', signup_doctor, name='signup_doctor'),
    path('login_Admin/', login3_admin, name='login_admin'),
    path('login_admin/', login_admin, name='login_admin'),
    path('signup_admin/', signup3_admin, name='signup_admin'),
    path('signup_admin/', signup_admin, name='signup_admin'),
    path('loginas/',loginas,name='loginas'),
]