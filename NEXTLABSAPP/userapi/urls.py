from django.urls import path
from .views import home,appdetails,UserProfile
urlpatterns=[
    path("home/",home),
    path("appdetails/<int:id>",appdetails),
    path("userprofile/",UserProfile)
]