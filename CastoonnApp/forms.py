from django import forms
from .models import User_Registration
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput


 ###################################################################################<<<<<<<<< Creator Userform >>>>>>>>>>>>>>>>>

class User_RegistrationForm(forms.ModelForm):

        # def clean(self):
        #     cleaned_data = super().clean()
        #     phone_number = cleaned_data.get('phone_number')
        #     email = cleaned_data.get('email')

        # # Validate phone number
        #     if phone_number:
        #         pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
        #         if not re.match(pattern, phone_number):
        #             self.add_error('phone_number', 'Invalid phone number')

        #     # Validate email address
        #     if email:
        #         email_validator = EmailValidator()
        #         try:
        #             email_validator(email)
        #         except ValidationError:
        #             self.add_error('email', 'Invalid email address')
        #             messages.error('Invalid email address')

        #     return cleaned_data


        gender = forms.ChoiceField(choices=[
            ('Gender', 'Gender'),
            ('Female', 'Female'),
            ('Male', 'Male'),
        ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
        
        # profession = forms.ChoiceField(choices=[
        #     ('Profession', 'Profession'),
        #     ('Actor', 'Actor'),
        #     ('Costume_Designer', 'Costume_Designer'),
            
        # ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))

        date_of_birth = forms.DateField(
             widget=forms.DateInput(attrs={'class': 'form-control item', 
                                           'id': 'birthday', 'placeholder': 'Date of Birth',
                                           'type': 'date',}))

        class Meta:
            model = User_Registration
            fields = '__all__'
        
            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Name'}),
                'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
                'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'phone number'}),
                'phone_otp': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Enter phone OTP'}),
                'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email','id':'email'}),
                'email_otp': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Enter Email OTP','id':'email_otp'}),
                'profession': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Profession'}),
                'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'}),
                'role': forms.HiddenInput(attrs={'value': 'PREFIX_VALUE','id': 'role-field'}),

                }
            
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].required = False
            self.fields['password'].required = False




