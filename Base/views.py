from django.shortcuts import render, HttpResponse
# from Post.models import Article, Category, Content

def showHome(request):
    return render(request, 'Base/index.html')
    # return HttpResponse("this is Home")

# def sidebar(request):
#     return render(request, "sidebar.html", {"Category": Category.objects.all(),
#                                             "Contents": Content.objects.all()})