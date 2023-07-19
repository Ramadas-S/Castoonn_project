from django.contrib import admin
from .models import User_Registration,Email_Validation

# Register your models here.

admin.site.register(User_Registration)
admin.site.register(Email_Validation)