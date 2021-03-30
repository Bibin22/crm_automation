from django.forms import ModelForm
from django import forms
from .models import Course,Batch,Enquiry, Admissions, Payment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BatchCreateForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_code', 'course_name', 'start_date', 'fees', 'status']
        widgets = {
            'batch_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.Select(attrs={'class': 'form-control'}),
            'Start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'fees': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

class CounsellorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),

        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class EnquiryCreateForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"

class AdmissionCreateForm(ModelForm):
    class Meta:
        model = Admissions
        fields = "__all__"

class StudentRegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"