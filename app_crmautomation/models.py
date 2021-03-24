from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20, unique=True)

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
        return self.course_name

class Enquiry(models.Model):
    student_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    followup_date = models.DateField()
    choices = (('admited', 'admited'), ('not admited','not admited'))
    status = models.CharField(max_length=20, choices=choices)
    def __str__(self):
        return self.student_name

class Admissions(models.Model):
    admission_number = models.IntegerField()
    enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    fees = models.IntegerField()
    def __str__(self):
        return self.admission_number
class Payment(models.Model):
    admission_number = models.ForeignKey(Admissions, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.admission_number
