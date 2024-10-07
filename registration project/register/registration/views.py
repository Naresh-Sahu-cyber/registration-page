from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import user

# Create your views here.
def user_home(request):
    if request.method=="POST":
        F_name=request.POST.get("F_name")
        L_name=request.POST.get("L_name")
        user_id=request.POST.get("user_id")
        occupation=request.POST.get("occupation")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        department=request.POST.get("department")
        working=request.POST.get("working")


        u=user()

        u.First_name=F_name
        u.L_name=L_name
        u.user_id=user_id
        u.occupation=occupation
        u.phone=phone
        u.email=email
        u.department=department
        if working is None:
            u.working=False
        else:
            u.working=True    

        u.save()    

        return redirect("/")
    return render(request ,'user_home.html')
   
def user_data(request):
    users=user.objects.all()
    return render(request,"user_data.html", {"users":users})

def delete_user(request, user_id):
    User= user.objects.get(pk=user_id)
    User.delete()
    return redirect("/registration/user-data/")

