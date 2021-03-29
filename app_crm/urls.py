from django.urls import path
from .views import Course_Registration, Course_View, Course_edit, Course_delete

urlpatterns = [
    path('course',Course_Registration.as_view(),name='course'),
    path('view_course',Course_View.as_view(),name='view_course'),
    path('course_edit/<int:id>', Course_edit.as_view(), name='course_edit'),
    path('course_delete/<int:id>', Course_delete.as_view(), name='course_delete'),
]

