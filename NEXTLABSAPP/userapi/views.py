from django.shortcuts import render,redirect
from baseapp.models import Users,Apps,Transactions,ActiveUser
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
@api_view(["GET"])
def home(request):
    m=Apps.objects.all()
    points=getTotalPoints()
    j=ActiveUser.objects.values("username").get(id=1)
    k={"App":m,"points":points,"name":j}
    return render(request,"userhome.html",k)
def getid():
    j=ActiveUser.objects.values("userid").get(id=1)
    return(j["userid"])

@api_view(["GET","POST"])
def appdetails(request,id):
    m=Apps.objects.all().get(id=id)
    points=getTotalPoints()
    j=ActiveUser.objects.values("username").get(id=1)
    j={"App":m,"points":points,"name":j}
    if(request.method=='POST'):
        screenshot=request.POST.get("photos")
        if screenshot=='':
            messages.info(request,'Please upload screenshot')
        else:
            m=Apps.objects.all().get(id=id)
            j=Transactions(AppId=id,UserId=getid(),TransactionPoints=m.Points,Image=screenshot)
            j.save()
            return redirect("/user/home")
    return render(request,"appdetails.html",j)
def getTotalPoints():
    n=Transactions.objects.filter(UserId=getid()).aggregate(Sum("TransactionPoints"))
    return n["TransactionPoints__sum"]

@api_view(["GET"])
def UserProfile(request):
    n=Users.objects.values("username","email").filter(id=getid())
    m=ActiveUser.objects.values("username").get(id=1)
    sum=getTotalPoints()
    t=Transactions.objects.values("AppId").filter(UserId=getid())
    appslist=[]
    for i in t:
        appslist.append(i["AppId"])
    k=Apps.objects.values("AppName").filter(id__in=appslist)
    j={"points":sum,"userdetails":n,"InstalledApps":k,"name":m}
    return render(request,"UserProfile.html",j)