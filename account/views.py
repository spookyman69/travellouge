from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("Login Successful")
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials.')
            print("Login Failed")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        emailid = request.POST['emailid']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username is already taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request, "Email is already taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=emailid, password=cpassword)
                user.save();
                print("user created")
                messages.info(request, "Registration Succesful")
                return render(request, 'login.html')
                #messages.info (request, "succesfuly")
                #messages.info (request, "username taken")
        else:
            messages.info(request, "Password does not match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
