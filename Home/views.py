from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Employee

# Create your views here.


def homepageviews(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        department = request.POST.get("department")
        address = request.POST.get("address")
        mobilenumber = request.POST.get("mobilenumber")
        email = request.POST.get("email")

        myuser = Employee.objects.create(
            Fullname=fullname,
            Department=department,
            Address=address,
            MobileNumber=mobilenumber,
            Email=email,
        )
        return redirect("details")
    return render(request, "index.html")


def details(request):
    myusers = Employee.objects.all()
    return render(request, "details.html", {"key1": myusers})


def update(request, id):
    update = Employee.objects.get(id=id)
    return render(request, "edit.html", {"key2": update})


def delete(request, id):
    delete = Employee.objects.get(id=id)
    delete.delete()
    return HttpResponseRedirect("/details")
