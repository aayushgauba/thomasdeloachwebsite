from django.shortcuts import render, redirect
from django.contrib import messages,auth,admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Create your views here.
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        
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
            return redirect(signup)
        elif(user.filter(username = username).count() != 0):
            return redirect(signup)
        else:
            user.create(username = username, first_name = firstname, email = email, last_name = lastname, password=password, is_staff=False, is_superuser = True)

    return render(request, 'admin/signup.html')