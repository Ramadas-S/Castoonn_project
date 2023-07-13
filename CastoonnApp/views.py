from django.shortcuts import render, redirect
from .forms import User_RegistrationForm
from .models import User_Registration
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from CastoonnApp import forms



# from .forms import ArtistUserForm


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
            creator_object = get_object_or_404(User_Registration, pk=user_id)
            creator_object.username=username
            creator_object.password = password
            creator_object.save()
            messages.success(request, 'Thank you for registering with us.  Please Create Username and Password.')
            return redirect('login_main')
        else:
            messages.success(request, ' Password and Confirm Password are not matching. Please verify it.')

            return render(request,'index\index_creator\index_creator_confirmation.html',{'user_id':user_id})

    return render(request,'index\index_creator\index_creator_confirmation.html',{'user_id':user_id})


# def verify_otp(request, user_id):
#     if request.method == 'POST':
#         entered_otp = request.POST['otp']
#         user_registration = User_Registration.objects.get(pk=user_id)

#         if entered_otp == user_registration.email_otp:
#             user_registration.email_verified = True
#             user_registration.save()

#             messages.success(request, 'OTP verified successfully.')
#             return redirect('success_page')
#         else:
#             # OTP is incorrect, show an error message
#             messages.error(request, 'Invalid OTP. Please try again.')
#             return render(request, 'otp_verification.html', {'user_id': user_id})

#     return render(request, 'otp_verification.html', {'user_id': user_id})





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
            print("sucess")
            creator_object = User_Registration.objects.get(pk=user_id)
            creator_object.username=username
            creator_object.password = password
            creator_object.save()
            return redirect('user_type')
        else:
            error_message = 'Password and Confirm Password do not match.'
            return render(request,'index\index_artist\index_artist_confirmation.html',{'error_message':error_message})

    return render(request,'index\index_artist\index_artist_confirmation.html',{'user_id':user_id})