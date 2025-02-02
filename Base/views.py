from django.shortcuts import render, HttpResponse

def showHome(request):
    return render(request, 'Base/index.html')
    # return HttpResponse("this is Home")

# def sidebar(request):
#     return render(request, "sidebar.html", {"Category": Category.objects.all(),
#                                             "Contents": Content.objects.all()})