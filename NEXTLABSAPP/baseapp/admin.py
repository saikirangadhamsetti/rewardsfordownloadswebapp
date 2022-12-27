from django.contrib import admin
from .models import Apps,Users,Transactions
# Register your models here.
admin.site.register(Apps)
admin.site.register(Users)
admin.site.register(Transactions)