from django.forms import ModelForm
from django import forms
from .models import Course,Batch,Enquiry,Admissions,Payment

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
