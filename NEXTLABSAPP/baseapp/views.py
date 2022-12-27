from django.shortcuts import render,redirect
from .forms import usersignupform,userloginform
from django.http import HttpResponseRedirect,HttpResponse
from .models import Users,ActiveUser
from django.contrib import messages
# Create your views here.
def signup(request):
    m={"signupform":usersignupform}
    if(request.method=='POST'):
        k=usersignupform(request.POST)
        if(Users.objects.filter(username=k.data['username'])):
             messages.info(request,'Username is already in use try different')
             return redirect("/")
        else:
            m=usersignupform(request.POST)
            m.save()
        return redirect("login/")
    return render(request,"baseapp/signup.html",m)

def login(request):
    form={"K":userloginform}
    if(request.method=='POST'):
        m=userloginform(request.POST)
        if(Users.objects.filter(username=m.data['username']) & Users.objects.filter(password=m.data['password']) & Users.objects.filter(type="user")):
            o=Users.objects.values("id","username").filter(username=m.data['username']) & Users.objects.values("id","username").filter(password=m.data['password'])
            ActiveUser(1,o[0]['id'],o[0]["username"]).save()
            return HttpResponseRedirect('/user/home')
        elif(Users.objects.filter(username=m.data['username']) & Users.objects.filter(password=m.data['password']) & Users.objects.filter(type="owner")):
            return HttpResponseRedirect("/owner/home")
        else:
            messages.info(request,'User does not exist')
    return render(request,"baseapp/login.html",form)
def logout(request):
    j=ActiveUser.objects.all().get(id=1)
    j.delete()
    return HttpResponse("User Logged Out Successfully")
