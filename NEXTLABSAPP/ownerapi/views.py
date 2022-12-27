from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer,TemplateHTMLRenderer
from baseapp.models import Apps,Transactions
from rest_framework import status
import requests
import django_tables2 as tables

@api_view(["POST"])
def saveappapi(request):
    if request.method=='POST':
        m=request.data
        k=Apps(
                AppName=m['AppName'],
                AppLink=m['AppLink'],
                AppCategory=m['AppCategory'],
                subcategory=m['subcategory'],
                AppImage=m['AppImage'],
                Points=m['Points']
                )
        
        k.save()
        return Response(status=status.HTTP_201_CREATED)
@api_view(["GET"])
def addapp(request):
    if request.method=='POST':
        AppImage=request.POST.get("imagelink")
        AppName=request.POST.get("appname")
        AppCategory=request.POST.get("appcategory")
        AppLink=request.POST.get("applink")
        subcategory=request.POST.get("subcategory")
        Points=int(request.POST.get("addpoints"))
        data={"AppName":AppName,"AppLink":AppLink,"AppCategory":AppCategory,"subcategory":subcategory,"AppImage":AppImage,"Points":Points}
        headers={'Content-Type':'application/json'}
        r=requests.post('http://127.0.0.1:8000/owner/saveappapi/',json=data,headers=headers)
        return render(request,"ownerhome.html")
    else:
        return render(request,"ownerhome.html")
class AppsTable(tables.Table):
   class Meta:
      model = Apps
class Appslist(tables.SingleTableView):
    table_class=AppsTable
    template_name="appslist.html"
    def get_queryset(self):
        return Apps.objects.all()
class TransactionTable(tables.Table):
   class Meta:
      model = Transactions
class Transactionslist(tables.SingleTableView):
    table_class=TransactionTable
    template_name="transactions.html"
    def get_queryset(self):
        return Transactions.objects.all()


