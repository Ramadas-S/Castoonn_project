from django.shortcuts import render, redirect
from .forms import User_RegistrationForm
from .models import User_Registration,Email_Validation,Creator_Profile
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from CastoonnApp import forms
from django.http import HttpResponse, JsonResponse

#for mailing functionality
import random
import string
from django.core.mail import send_mail





######################################################################### <<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>
def index(request):
    return render(request, 'index/index.html')

def login_main(request):
    return render(request,'index/login.html')

def user_type(request):
    return render(request, 'index/user_type.html')



######################################################################### <<<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>
def creator_registration(request):

    if request.method =='POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            nickname = form.cleaned_data['nickname']
            gender = form.cleaned_data['gender']
            profession = form.cleaned_data['profession']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']
            phone_otp = form.cleaned_data['phone_otp']
            email = form.cleaned_data['email']
            email_otp = form.cleaned_data['email_otp']
            experience = form.cleaned_data['experience']
            role = form.cleaned_data['role']
            user_registration = User_Registration(
                name=name,
                lastname=lastname,
                nickname=nickname,
                gender=gender,
                profession=profession,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                phone_otp=phone_otp,
                email=email,
                email_otp=email_otp,
                experience=experience,
                role=role
            )
            user_registration.save()
            user_id = user_registration.pk
            return redirect('index_creator_confirmation',user_id=user_id)
    else:
        form = User_RegistrationForm()
        form.initial['role'] = 'user1'
    return render(request,'index\index_creator\index_creator_registraion.html',{'form':form})



def index_creator_confirmation(request,user_id):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User_Registration.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('index_creator_confirmation', user_id=user_id)
            else:
                creator_object = get_object_or_404(User_Registration, pk=user_id)
                creator_object.username=username
                creator_object.password = password
                creator_object.save()
                messages.success(request, 'Thank you for registering with us.')
                request.session['userid'] = user_id
            return redirect('profile_creator')
        else:
            messages.error(request, ' Password and Confirm Password are not matching. Please verify it.')
            return redirect('index_creator_confirmation', user_id=user_id)

    return render(request,'index\index_creator\index_creator_confirmation.html',{'user_id':user_id})


######################################################################### <<<<<<<<<< Email Verification >>>>>>>>>>>>>>

def email_send(request):
    digits = string.digits
    otp = ''.join(random.choices(digits, k=6))
    email = request.GET.get('inputValue')
    user_email = Email_Validation.objects.create(email_temp=email,email_otp_temp=otp)
    user_email.save()
    subject = 'Catoonn Email Verification OTP'
    message = f'Hi {email},\nYour Email Verification OTP is: {otp}'
    from_email = 'email'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def verify_email_otp(request):
    email=request.GET.get('emailValue')
    otp=request.GET.get('otpValue')
    print(otp)
    print(email)
    instance = get_object_or_404(Email_Validation,email_otp_temp=otp)
    if instance.email_temp == email:
        result="Email Verified"
    else:
        result="Your Entered Otp Is Incorrect"
    print(result)
    return JsonResponse({"status": " not", 'result':result})
                         

######################################################################### <<<<<<<<<< ARTIST MODULE >>>>>>>>>>>>>>>>

def artist_registration(request):

    if request.method =='POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():
            user_model=form.save()
            user_id = user_model.pk
            return redirect('index_artist_confirmation',user_id=user_id)
    else:
        form = User_RegistrationForm()
        form.initial['role'] = 'user2'
    return render(request,'index\index_artist\index_artist_registraion.html',{'form':form})


def index_artist_confirmation(request,user_id):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print("success")
            if User_Registration.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('index_artist_confirmation', user_id=user_id)
            else:
                artist_object = get_object_or_404(User_Registration, pk=user_id)
                artist_object.username=username
                artist_object.password = password
                artist_object.save()
                messages.success(request, 'Thank you for registering with us.')
                return redirect('login_main')
        else:
            messages.error(request, ' Password and Confirm Password are not matching. Please verify it.')
            return redirect('index_artist_confirmation', user_id=user_id)

    return render(request,'index\index_artist\index_artist_confirmation.html',{'user_id':user_id})
######################################################################### <<<<<<<<<< CREATOR PROFILE MODULE >>>>>>>>>>>>>>>>

def profile_creator(request):
    if request.session.has_key('userid'):
        pass
    else:
        return redirect('/')
    
    pk=request.session['userid']
    user = get_object_or_404(User_Registration,pk=pk)

    if request.method == 'POST':
        form_data = request.POST.dict()
        user_image = request.FILES.get('image', None)
        firstname = form_data.get('firstname', None)
        lastname = form_data.get('lastname', None)
        address = form_data.get('address', None)
        phonenumber = form_data.get('phonenumber', None)
        email = form_data.get('email', None)
        gender = form_data.get('gender', None)
        date_of_birth = form_data.get('date_of_birth', None)
        marital_status = form_data.get('marital_status', None)
        profection = form_data.get('profection', None)
        height = form_data.get('height', None)
        weight = form_data.get('weight', None)
        interests = form_data.get('interests', None)
        hobbies = form_data.get('hobbies', None)
        passions = form_data.get('passions', None)
        goals = form_data.get('goals', None)
        achievements = form_data.get('achievements', None)
        social_media_links = form_data.get('social_media_links', None)
        skills = form_data.get('skills', None)
        awards = form_data.get('awards', None)
        more_abt_u = form_data.get('message', None)
        
        new_creator_profile = Creator_Profile(
            user = user,
            user_image=user_image,
            firstname=firstname,
            lastname=lastname,
            address=address,
            phonenumber=phonenumber,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            marital_status=marital_status,
            profection=profection,
            height=height,
            weight=weight,
            interests=interests,
            hobbies=hobbies,
            passions=passions,
            goals=goals,
            achievements=achievements,
            social_media_links=social_media_links,
            skills=skills,
            awards=awards,
            more_abt_u=more_abt_u,
        )
        new_creator_profile.save()
        return redirect('user_type')
    
    context={
        'user':user
    }

    return render(request,'creator\profile_creator.html',context)


