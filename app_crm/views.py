from django.shortcuts import render, redirect
from .models import Course,Batch, Enquiry,Admissions,Payment
from django.views.generic import TemplateView
from .forms import CourseCreateForm

class Course_Registration(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'app_crm/ch_course_registration.html'
    def get(self, request, *args, **kwargs):
        self.context ={
            "form":self.form_class
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_course')
        else:
            self.context = {
                "form":self.form_class
            }
            return render(request, self.template_name, self.context)


class Course_View(TemplateView):
    model = Course
    template_name = 'app_crm/ch_course_registration.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        self.context = {
            "courses":courses
        }
        return render(request, self.template_name, self.context)

class Course_edit(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'app_crm/ch_course_registration.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(instance=courses)
        self.context = {
            "form":form
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('view_course')
        return render(request, self.template_name, self.context)

class Course_delete(TemplateView):
    model = Course
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        course = self.get_object(id)
        course.delete()
        return redirect('view_course')



