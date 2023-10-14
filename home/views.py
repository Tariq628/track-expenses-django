from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

@login_required(login_url="login")
def index(request):
    return render(request, "home.html")


def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return render(request, "login.html")
    return render(request, "login.html")


def reg(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already taken")
                return redirect("/register/")
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "email taken")
                return redirect("/register/")

            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.success(request, "Successfully registered you can login now.")
                return redirect("/")

        else:
            messages.warning(request, "password not matching.")
            return redirect("/register/")

        # print('password not matching.')
    else:
        return render(request, "register.html")


def logoutuser(request):
    logout(request)
    return redirect("/login/")


"""
RESET PASSWORD
"""
def reset_password(request):
    return PasswordResetView.as_view(template_name="reset_password.html")(request)


def reset_password_done(request):
    return PasswordResetDoneView.as_view(template_name="password_reset_done.html")(
        request
    )


def reset_password_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"
    )(request, uidb64=uidb64, token=token)


def reset_password_complete(request):
    return PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    )(request)
