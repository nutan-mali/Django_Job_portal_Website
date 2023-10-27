from django.contrib import admin
from app1.models import jobPost , jobSearch , Contact
# Register your models here.
admin.site.register(jobPost) #Register my model jobpost in adminpy.
admin.site.register(jobSearch) 
admin.site.register(Contact) 