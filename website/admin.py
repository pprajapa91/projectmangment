from django.contrib import admin

# Register your models here.
from .models import userLogin,addProject,addtask
admin.site.register(userLogin)
admin.site.register(addProject)
admin.site.register(addtask)



