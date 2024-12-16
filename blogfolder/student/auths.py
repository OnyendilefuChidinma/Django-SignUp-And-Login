from email import message
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.mixins import LoginRequiredMixin

class Signup(View):
    # template_name = 'auth/signup.html'

    def get(self, request):
        # return redirect(request, 'auth/signup.html')
        return render(request, 'auth/signup.html')
        # return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'auth/signup.html')
            # return HttpResponse('Passwords do not match')

        if email:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'auth/signup.html')
                # return HttpResponse('Email already exists')



        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'auth/signup.html')
            # return HttpResponse('Username already exists')
        
        # print(username, last_name, first_name, email, password, confirm_password)
        user = User.objects.create_user(username=username, last_name=last_name, first_name=first_name, email=email, password=password)


        if user:
            # user.save()
            messages.success(request, 'Username created')
            return redirect('dashboardView')
            # return render(request, 'cohorts/index.html')
            # return HttpResponse('Username created')
            # return render(request, 'auth/login.html')
            # return redirect('auth/login.html')

        return render(request, 'auth/signup.html')   

class Login(View):
    def get(self, request):
        return render(request, 'auth/login.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # user = User.objects.filter(username=username).first()
        # if user:
        #     if user.check_password(password):
        #         return redirect('dashboardView')
        #     else:
        #         messages.error(request, 'Wrong password')
        #         return render(request, 'auth/login.html')
        # else:
        #     messages.error(request, 'Username does not exist')
        #     return render(request, 'auth/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'Login successful! Welcome back, ' + user.first_name + ' ' + user.last_name + '.')
            messages.success(request, f'Login successful! Welcome back, {user.first_name} {user.last_name}.')
            # messages.success(request, f'Login successful! Welcome back, {username}.')
            return redirect('dashboardView')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'auth/login.html')

        # return render(request, 'auth/login.html')

class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('login')




# def signup(request):
#     return render(request, 'auth/signup.html')