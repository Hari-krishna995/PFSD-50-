from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.
def newhomepage(request):
    return render(request,'homepage.html')
def homepage(request):
    return render(request,'newhomepage.html')

def Contactus(request):
    return render(request,'contactus.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'signup.html')

def login2_doctor(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'homepage_doctor.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def login_doctor(request):
    return render(request, 'login.html')

def signup_doctor(request):
    return render(request, 'signup.html')

def signup2_doctor(request):
    if request.method == "POST":
        doctorusername = request.POST['doctorusername']
        doctorpass1 = request.POST['doctorpassword']
        doctorpass2 = request.POST['doctorpassword1']
        if doctorpass1 == doctorpass2:
            if User.objects.filter(username=doctorusername).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'signup_doctor.html')
            else:
                user = User.objects.create_user(username=doctorusername, password=doctorpass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login_doctor.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'signup_doctor.html')

def login3_admin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'homepage_admin.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login_admin.html')

    else:
        return render(request,'login_admin.html')

def login_admin(request):
    return render(request, 'login_admin.html')

def signup_admin(request):
    return render(request, 'signup_admin.html')

def signup3_admin(request):
    if request.method == "POST":
        adminusername = request.POST['adminusername']
        adminpass1 = request.POST['adminpassword']
        adminpass2 = request.POST['adminpassword1']
        if adminpass1 == adminpass2:
            if User.objects.filter(username=adminusername).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'signup_admin.html')
            else:
                user = User.objects.create_user(username=adminusername, password=adminpass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login_admin.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'signup_admin.html')

def logout(request):
    auth.logout(request)
    return render(request, 'homepage.html')

def feedbackfunction(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comments = form.cleaned_data['comments']
            tosend='Name:'+name+'\nEmail:'+email+'\nProblem:'+comments+'_this is the problem statement from customer.'

            # Save feedback data to the database
            feedback = Feedback(name=name, email=email, comments=comments)
            feedback.save()
            var='sivaganeshyasam@gmail.com'
            send_mail(
                'Please give the appropiate solution for the given problem.',
                tosend,
                 'sivaganeshyasam@gmail.com',
                   [var],
                fail_silently=False,
            )
            # Display a success message
            messages.success(request, ' Mail sended  successfully.')

            return redirect('/')  # Change 'thank_you_page' to the actual URL or name of your thank you page

        else:
            form = FeedbackForm()

        return render(request, 'contactus.html', {'form': form})
def feedback(request):
    return render(request, 'contactus.html')

def AboutUs(request):
    return render(request,'Aboutus.html')

def loginas(request):
    return render(request,'loginas.html')