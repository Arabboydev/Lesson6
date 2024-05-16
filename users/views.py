from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
        return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form =AuthenticationForm()
        context = {
            'form':login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing_page')
        return render(request, 'login.html', context={'form': login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')



# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'register.html')
#
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#
#         user = CustomUser.objects.create_user(
#             username=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         return redirect('users:login')
