from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Courses
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')
    


def courses(request):
    if request.user.is_authenticated :

        cc = Courses.objects.all()
        return render(request,'courses.html',{'cc' : cc})
    else:
        messages.info(request,'Login to view courses')
        return redirect('login')




def signup(request):


    if request.method == 'POST':
       
        user_name = request.POST['username']
        email     = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name, password=password1,email=email)
                user.save()
                messages.info(request,'account created')
                return redirect('signup')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')

        return redirect('/')
        
    else:
            return render(request,'signup.html')    



    


def login(request):

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('courses')
        else:
            messages.info(request,"Invalid username or password")    
            return redirect('login')

    else:
        return render(request,'login.html')



def logout(request):

    auth.logout(request)
    return redirect('/')


