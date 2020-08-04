from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from app_project.models import CustomUser, Supervisor


def admin_home(request):
    return render(request, "admin_template/home_content.html")


def add_supervisor(request):
    return render(request, "admin_template/add_supervisor.html")


def add_supervisor_save(request):
    if request.method != "POST":
        return HttpResponse("Method is Not POST")
    else:
        first_name = request.POST.get("fist_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
#         now creating customuser object by method .creae_user()
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=2)
            user.supervisor.address = address
            user.save()
            messages.success("Add Supervisor Successfully")
            return HttpResponseRedirect(request, "/add_supervisor")
        except:
            messages.error(request, "Add Supervisor Successfully")
            return HttpResponseRedirect("/add_supervisor")


