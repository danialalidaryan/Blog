from django.shortcuts import render, redirect, HttpResponse
from .forms import signupForm
from .models import EmailAddress
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# def userProfile(request, slug):
#     return render(request, "Accounting/userProfile.html", context={
#         "user": Profile.objects.all().filter(slug=slug)[0]
#     })

def signup_View(request):
    if request.user.is_authenticated:
        return redirect("Base:home")

    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            Email = EmailAddress.objects.create(User=None, Email=form.cleaned_data['temp_email'], Is_Default=True)
            user.Email = Email
            user.set_password(form.cleaned_data['password1'])
            user.save()
            Email.User = user
            Email.save()
            return HttpResponse("Successful")
        else:
            print(form.errors)
    else:
        form = signupForm()
    return render(request, "registration/signup.html", context={"form": form})

def signin_View(request):
    if request.user.is_authenticated:
        return redirect("Base:home")


    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("Log in successful")  # صفحه اصلی پس از ورود
            else:
                form.add_error(None, "نام کاربری یا رمز عبور اشتباه است.")
        else:
            pass
    else:
        form = AuthenticationForm()

    return render(request, 'account_app/test.html', {'form': form})

def signout_View(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("Base:home")
    else:
        return redirect("Base:home")