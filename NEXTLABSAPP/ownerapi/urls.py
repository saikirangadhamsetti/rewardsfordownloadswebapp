from django.urls import path
from .views import saveappapi,addapp,Appslist,Transactionslist
urlpatterns=[
    path("appslist/",Appslist.as_view()),
    path("home/",addapp),
    path("",addapp),
    path("saveappapi/",saveappapi),
    path("transactionlist/",Transactionslist.as_view())
]