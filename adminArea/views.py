from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from django.contrib import messages,auth,admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
    return False

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('adminHome')
    return render(request, 'admin/signin.html')

def signup(request):
    user = User.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('password2')

        if(password != passwordcheck):
            messages.error(request, 'Passswords dont match')
            return redirect(signup)
        if(user.filter(username = username).count() != 0):
            messages.error(request, 'Username already exists')
            return redirect(signup)
        if(isValidEmail(email) == False):
            messages.error(request, 'Please enter a valid email')
            return redirect(signup)
        if(firstname == ""):
            messages.error(request, 'Please enter a First Name')
            return redirect(signup)
        if(lastname == ""):
            messages.error(request, 'Please enter a Last Name')
            return redirect(signup)
        if(username == ""):
            messages.error(request, 'Please enter a Username')
            return redirect(signup)

        else:
            user.create(username = username, first_name = firstname, email = email, last_name = lastname, password=password, is_staff=False, is_superuser = True)

    return render(request, 'admin/signup.html')