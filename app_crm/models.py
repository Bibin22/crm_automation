from django.db import models
from datetime import date
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=20, unique=True)
    course_duration = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    batch_code = models.CharField(max_length=20, unique=True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    fees = models.IntegerField()
    choices = (('yet to begin', 'yet to begin'), ('in progress', 'in progress'), ('completed', 'completed'))
    status = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.batch_code

class Enquiry(models.Model):
    enquiry_id = models.CharField(primary_key=True, editable=False, max_length=20)
    student_name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    qualification = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    followup_date = models.DateField()
    choices = (('admited', 'admited'), ('not admited','not admited'))
    status = models.CharField(max_length=20, choices=choices)
    def __str__(self):
        return str(self.enquiry_id)

class Admissions(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    eid = models.ForeignKey(Enquiry,on_delete=models.CASCADE)
    fees = models.IntegerField()
    batch_code = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    def __str__(self):
        return self.admission_number
class Payment(models.Model):
    admission_number = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    eid = models.ForeignKey(Enquiry, on_delete=models.CASCADE)

    def __str__(self):
        return self.admission_number
