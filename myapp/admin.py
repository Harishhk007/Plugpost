from django.contrib import admin
from .models import Users
from .models import Blogs
# Register your models here.
@admin.register(Users)
class Users(admin.ModelAdmin):
    
    pass

@admin.register(Blogs)
class Blogs(admin.ModelAdmin):
    
    pass
