# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages

# Create your views here.

# def loginForm(request):
#     if request.user.is_authenticated:
#         return redirect("home_app:Home")
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         repassword = request.POST.get('repassword')
#         if username and password and email and repassword:
#             context = {
#                 "errors": []
#             }
#             if user_authentication(username, email, password, repassword, context):
#                 user = User.objects.create(username=username, password=password, email=email)
#                 messages.success(request, "The user has created")
#             else:
#                 return render(request, 'accounting/loginForm.html', context)
#
#         elif username and password:
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home_app:Home')
#             else:
#                 messages.success(request, "The user has not found!")
#                 return redirect("accounting:Login")
#
#     return render(request, "accounting/loginForm.html", context={})
#
#
# def user_logout(request):
#     logout(request)
#     return redirect("home_app:Home")
#
#
# def user_authentication(username, email, password, repassword, context):
#     flag = True
#     if password != repassword:
#         context["errors"].append("Passwords are not same")
#         flag = False
#     try:
#         if User.objects.get(username=username):
#             context["errors"].append("This username is exists")
#             flag = False
#     except:
#         pass
#     try:
#         if User.objects.get(email=email):
#             context["errors"].append("This email used by another user")
#             flag = False
#     except:
#         pass
#     return flag
#
#
# def userProfile(request, slug):
#     return render(request, "accounting/userProfile.html", context={
#         "user": Profile.objects.all().filter(slug=slug)[0]
#     })
