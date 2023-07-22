from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class User_Registration(models.Model):
    
    name = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    nickname = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=20)
    phone_otp = models.IntegerField(null=True,blank=True)
    email = models.EmailField(unique=True)
    email_otp =models.IntegerField(null=True,blank=True)
    profession = models.CharField(max_length=255,blank=True,null=True)
    experience = models.IntegerField(null=True)
    role = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.nickname

# Test 
class Email_Validation(models.Model):
    email_temp = models.EmailField()
    email_otp_temp =models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.email_temp + " " + str(self.email_otp_temp) 


 ###################################################################################<<<<<<<<< Model for Creator Profile form>>>>>>>>>>>>>>>>>

class Creator_Profile(models.Model):
    user = models.ForeignKey(User_Registration, on_delete=models.SET_NULL, null=True, blank=True)
    user_image = models.ImageField(upload_to='photos/', blank=True)
    firstname = models.CharField(max_length=255,blank=True,null=True)
    lastname = models.CharField(max_length=255,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=255,blank=True,null=True)
    date_of_birth = models.DateField(null=True)
    marital_status = models.CharField(max_length=255,blank=True,null=True)
    profection = models.CharField(max_length=255,blank=True,null=True)
    height = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    interests = models.TextField(blank=True,null=True)
    hobbies = models.TextField(blank=True,null=True)
    passions = models.TextField(blank=True,null=True)
    goals = models.TextField(blank=True,null=True)
    achievements = models.TextField(blank=True,null=True)
    social_media_links = models.TextField(blank=True,null=True)
    skills = models.TextField(blank=True,null=True)
    awards = models.TextField(blank=True,null=True)
    more_abt_u = models.TextField(blank=True,null=True)

    
    def __str__(self):
        return f"{self.firstname}"


 ###################################################################################<<<<<<<<< Model for Artist registration form >>>>>>>>>>>>>>>>>





###################################################################################<<<<<<<<< Confirm registration for creator >>>>>>>>>>>>>>>>>




###################################################################################<<<<<<<<< Confirm registration for Artist >>>>>>>>>>>>>>>>>


