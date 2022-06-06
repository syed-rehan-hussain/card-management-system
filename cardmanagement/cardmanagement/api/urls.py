from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('section/', SectionCreateView.as_view(), name='section_create'),
    path('section/', SectionCreateView.as_view(), name='section_get'),
    path('section/<int:pk>', SectionView.as_view(), name='section'),
    path('semester/', SemesterCreateView.as_view(), name='semester_create'),
    path('semesters/', SemesterCreateView.as_view(), name='semester_get'),
    path('semester/<int:pk>', SemesterView.as_view(), name='semester'),
    path('course/', CourseCreateView.as_view(), name='course_create'),
    path('course/', CourseCreateView.as_view(), name='course_get'),
    path('course/<int:pk>', CourseView.as_view(), name='course'),
    path('department/', DepartmentCreateView.as_view(), name='department_create'),
    path('department/', DepartmentCreateView.as_view(), name='department_get'),
    path('department/<int:pk>', DepartmentView.as_view(), name='department'),
    path('student/', StudentCreateView.as_view(), name='student_create'),
    path('student/<int:pk>', StudentView.as_view(), name='student'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)