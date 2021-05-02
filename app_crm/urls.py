from django.urls import path
from .views import Course_Registration, Course_edit, Course_delete, Batch_Creation, Batch_edit, Batch_delete,\
    CounsellorRegistration, CounsellorLogin, Counsellor_View, Counsellor_Edit, Counsellor_Delete, Enquiry_Creation, \
    Enquiry_Edit, Enquiry_Delete, Follow_up, Admission_Creation, Admission_Edit, Admission_Delete,Student_Details, \
    Student_Registration, Student_login, Student_Payments, DashBoard,load_course

urlpatterns = [
    path('course',Course_Registration.as_view(),name='course'),
    path('course_edit/<int:id>', Course_edit.as_view(), name='course_edit'),
    path('course_delete/<int:id>', Course_delete.as_view(), name='course_delete'),
    path('batch',Batch_Creation.as_view(),name='batch'),
    path('batch_edit/<int:id>', Batch_edit.as_view(), name='batch_edit'),
    path('batch_delete/<int:id>', Batch_delete.as_view(), name='batch_delete'),
    path('cs_register', CounsellorRegistration.as_view(), name='cs_register'),
    path('cs_login', CounsellorLogin.as_view(), name='cs_login'),
    path('cs_view', Counsellor_View.as_view(), name='cs_view'),
    path('cs_edit/<int:id>', Counsellor_Edit.as_view(), name='cs_edit'),
    path('cs_delete/<int:id>', Counsellor_Delete.as_view(), name='cs_delete'),
    path('enquiry', Enquiry_Creation.as_view(), name='enquiry'),
    path('enquiry_edit/<int:id>', Enquiry_Edit.as_view(), name='enquiry_edit'),
    path('enquiry_delete/<int:id>', Enquiry_Delete.as_view(), name='enquiry_delete'),
    path('admission/<int:id>', Admission_Creation.as_view(), name='admission'),
    path('admission_edit/<int:id>', Admission_Edit.as_view(), name='admission_edit'),
    path('admission_delete/<int:id>', Admission_Delete.as_view(), name='admission_delete'),
    path('followup', Follow_up.as_view(), name='followup'),
    path('st_view<int:id>', Student_Details.as_view(), name='st_view'),
    path('st_register<int:id>', Student_Registration.as_view(), name='st_register'),
    path('st_login', Student_login.as_view(), name='st_login'),
    path('pay', Student_Payments.as_view(), name='pay'),
    path('home', DashBoard.as_view(), name='home'),
    path('ajax/load-course/',load_course, name='ajax_load_course'),
]

