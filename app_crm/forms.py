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
            'start_date': forms.TextInput(attrs={'class': 'form-control'}),
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
        widgets = {
            'enquiry_id': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'followup_date': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }


class AdmissionCreateForm(ModelForm):
    class Meta:
        model = Admissions
        fields = "__all__"

        widgets = {
           'admission_number': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
           'eid': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
           'fees': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_code': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'date': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),

        }

class StudentRegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
        }
class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

        widgets = {
            'admission_number': forms.TextInput(attrs={'class': 'form-control shadow-none bg-light', 'readonly':'readonly'}),
            'amount': forms.TextInput(attrs={'class': 'form-control shadow-none bg-light'}),
            'date': forms.TextInput(attrs={'class': 'form-control','readonly shadow-none bg-light': 'readonly'}),
            'eid': forms.TextInput(attrs={'class': 'form-control','readonly shadow-none bg-light': 'readonly'}),


        }