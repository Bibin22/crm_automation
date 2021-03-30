from django.shortcuts import render, redirect, HttpResponse
from .models import Course,Batch, Enquiry, Admissions,Payment
from django.views.generic import TemplateView
from .forms import CourseCreateForm, BatchCreateForm, CounsellorRegistrationForm, LoginForm, EnquiryCreateForm,\
    AdmissionCreateForm, StudentRegistraionForm, PaymentCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
class Course_Registration(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'app_crm/ch_course_registration.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        self.context = {
            "form":self.form_class,
            "courses":courses
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            courses = Course.objects.all()
            self.context = {
                "form": self.form_class,
                "courses": courses
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form":self.form_class
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
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('course')
        return render(request, self.template_name, self.context)

class Course_delete(TemplateView):
    model = Course
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        course = self.get_object(id)
        course.delete()
        return redirect('course')

class Batch_Creation(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'app_crm/ch_batch_creation.html'

    def get(self, request, *args, **kwargs):
        batches = Batch.objects.all()
        self.context = {
            "form": self.form_class,
            "batches": batches
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            batches = Batch.objects.all()
            self.context = {
                "form": self.form_class,
                "batches": batches
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

class Batch_edit(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'app_crm/ch_batch_creation.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(instance=batches)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(request.POST, instance=batches)
        if form.is_valid():
            form.save()
            return redirect('batch')
        return render(request, self.template_name, self.context)

class Batch_delete(TemplateView):
    model = Batch
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batch = self.get_object(id)
        batch.delete()
        return redirect('batch')

class CounsellorRegistration(TemplateView):
    form_class = CounsellorRegistrationForm
    template_name = 'app_crm/ch_counsellor_registration.html'
    def get(self, request, *args, **kwargs):
        self.context = {
            "form":self.form_class
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cs_login')
        else:
            self.context = {
                "form":form
            }
            return render(request, self.template_name, self.context)

class CounsellorLogin(TemplateView):
    form_class = LoginForm
    template_name = 'app_crm/cs_login.html'
    def get(self, request, *args, **kwargs):
        self.context = {
            "form":self.form_class
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request,user)
                return redirect('enquiry')
            else:
                self.context = {
                    "form":form
                }
                return render(request, self.template_name, self.context)

class Counsellor_View(TemplateView):
    model = User
    template_name = 'app_crm/ch_counsellors.html'
    def get(self, request, *args, **kwargs):
        counsellors = User.objects.all()
        self.context = {
            "counsellors":counsellors
        }
        return render(request, self.template_name, self.context)

class Counsellor_Edit(TemplateView):
    model = User
    form_class = CounsellorRegistrationForm
    template_name = 'app_crm/ch_counsellor_registration.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        counsellors = self.get_object(id)
        form = self.form_class(instance=counsellors)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        counsellors = self.get_object(id)
        form = self.form_class(request.POST, instance=counsellors)
        if form.is_valid():
            form.save()
            return redirect('cs_view')
        return render(request, self.template_name, self.context)

class Counsellor_Delete(TemplateView):
    model = User

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        cs = self.get_object(id)
        cs.delete()
        return redirect('cs_view')

class Enquiry_Creation(TemplateView):
    model = Enquiry
    form_class = EnquiryCreateForm
    template_name = 'app_crm/cs_student_enquiry.html'
    def get(self, request, *args, **kwargs):
        enquiry = self.model.objects.last()
        if enquiry:
            last_eid = enquiry.enquiry_id
            lst = int(last_eid.split('-')[1]) + 1
            eid = 'EID-' + str(lst)
        else:
            eid = 'EID-1000'
        form = self.form_class(initial={'enquiry_id': eid})
        students = Enquiry.objects.all()
        self.context = {
           "students":students,
            "form":form,
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            students = Enquiry.objects.all()
            self.context = {
                "form": self.form_class,
                "students": students
            }
            return redirect('enquiry')
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

class Enquiry_Edit(TemplateView):
    model = Enquiry
    form_class = EnquiryCreateForm
    template_name = 'app_crm/cs_student_enquiry.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(instance=students)
        self.context = {
            "form":form,
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(request.POST, instance=students)
        if form.is_valid():
            #eid = form.cleaned_data.get("enquiry_id")

            form.save()
            return redirect('enquiry')
        return render(request, self.template_name, self.context)

class Enquiry_Delete(TemplateView):
    model = Enquiry

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        student = self.get_object(id)
        student.delete()
        return redirect('enquiry')

class Follow_up(TemplateView):
    model = Enquiry
    template_name = "app_crm/cs_follow_up_date.html"
    def get(self, request, *args, **kwargs):
        dates = Enquiry.objects.filter(followup_date=date.today())
        self.context = {
            "dates":dates
        }
        return render(request, self.template_name, self.context)

class Admission_Creation(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'app_crm/cs_admissions.html'

    def get_object(self, id):
        return Enquiry.objects.get(id=id)




    def get(self, request, *args, **kwargs):
        admission = self.model.objects.last()
        id = kwargs.get("id")
        students = self.get_object(id)

        if admission:
            last_adm = admission.admission_number
            lst = int(last_adm.split('-')[1]) + 1
            adm = 'LMNR-' + str(lst)
        else:
            adm = 'LMNR-1000'
        admissions = Admissions.objects.all()
        eid = students.enquiry_id
        batch = students.batch
        form = self.form_class(initial={'admission_number': adm,'eid':eid, 'batch_code':batch})

        self.context = {
            "admissions": admissions,
            "form": form,
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            admissions = Admissions.objects.all()
            self.context = {
                "form": self.form_class,
                "admissions": admissions
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

class Admission_Edit(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'app_crm/cs_admissions.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        form = self.form_class(instance=admissions)
        self.context = {
            "form":form,
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        form = self.form_class(request.POST, instance=admissions)
        if form.is_valid():
            form.save()
            admissions = Admissions.objects.all()
            self.context = {
                "form": self.form_class,
                "admissions": admissions
            }
            return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

class Admission_Delete(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'app_crm/cs_admissions.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admission = self.get_object(id)
        admission.delete()
        admissions = Admissions.objects.all()
        self.context = {
            "form": self.form_class,
            "admissions": admissions
        }
        return render(request, self.template_name, self.context)

class Student_Details(TemplateView):
    model = Admissions
    template_name = 'app_crm/cs_student_details.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        eid = admissions.eid

        students = Enquiry.objects.get(enquiry_id=eid)
        self.context = {
            'admissions':admissions,
            'students':students
        }
        return render(request, self.template_name, self.context)

class Student_Registration(TemplateView):
    form_class = StudentRegistraionForm
    template_name = 'app_crm/ch_counsellor_registration.html'
    def get_object(self, id):
        return Admissions.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admission = self.get_object(id)
        admission_number = admission.admission_number
        eid = admission.eid
        form = self.form_class(initial={'username': admission_number, 'password1': eid })
        self.context = {
            "form":form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('st_login')
        else:
            self.context = {
                "form": form
            }
            return render(request, self.template_name, self.context)

class Student_login(TemplateView):
    form_class = LoginForm
    template_name = 'app_crm/cs_login.html'

    def get(self, request, *args, **kwargs):
        self.context = {
            "form": self.form_class
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return render(request, 'app_crm/st_home.html')
            else:
                self.context = {
                    "form": form
                }
                return render(request, self.template_name, self.context)

class Student_Payments(TemplateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = 'app_crm/st_payment.html'
    def get(self, request, *args, **kwargs):
        admission = Admissions.objects.get(admission_number=request.user)
        admission_number = admission.admission_number

        eid = admission.eid

        form = self.form_class(initial={'admission_number': admission_number, 'eid': eid})
        #payments = Payment.objects.get(admission_number=request.user)
        self.context = {
            "form": form,
            #"payments":payments
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #payments = Payment.objects.get(admission_number=request.user)
            self.context = {
                "form": self.form_class,
                #"payments": payments
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)






