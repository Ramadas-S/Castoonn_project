from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.core.mail import send_mail

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

    # def generate_email_otp(self):
    #     otp = ''.join(random.choices(string.digits, k=6))
    #     self.email_otp = otp
    #     self.save()
    #     self.send_email_otp()
    
    # def send_email_otp(self):
    #     subject = 'Email Verification OTP'
    #     message = f'Your OTP for email verification is: {self.email_otp}'
    #     from_email = 'your_email@example.com'
    #     recipient_list = [self.email]

    #     send_mail(subject, message, from_email, recipient_list)
 


    def __str__(self):
        return self.nickname



 ###################################################################################<<<<<<<<< Model for Creator registration form>>>>>>>>>>>>>>>>>






 ###################################################################################<<<<<<<<< Model for Artist registration form >>>>>>>>>>>>>>>>>





###################################################################################<<<<<<<<< Confirm registration for creator >>>>>>>>>>>>>>>>>




###################################################################################<<<<<<<<< Confirm registration for Artist >>>>>>>>>>>>>>>>>


