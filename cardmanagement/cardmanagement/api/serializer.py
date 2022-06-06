from rest_framework import serializers
from rest_framework.fields import empty

from .models import *


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class SectionSerializer(serializers.ModelSerializer):
    section_no = serializers.CharField()
    section_year = serializers.CharField()

    class Meta:
        model = Section
        fields = ['id', 'section_no', 'section_year']


class SemesterSerializer(serializers.ModelSerializer):
    semester = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    section_id = serializers.IntegerField()
    course_id = serializers.IntegerField()

    class Meta:
        model = Semester
        fields = ['id', 'semester', 'start_date', 'end_date', 'section_id', 'course_id']


class CourseSerializer(serializers.ModelSerializer):
    course_name = models.CharField()
    description = models.CharField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description']


class DepartmentSerializer(serializers.ModelSerializer):
    dept_name = models.CharField()
    dept_code = models.CharField()
    phone = models.CharField()

    class Meta:
        model = Department
        fields = ['id', 'dept_name', 'dept_code', 'phone']


class StudentSerializer(serializers.ModelSerializer):
    first_name = models.CharField()
    last_name = models.CharField()
    father_name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
    address = models.CharField()
    password = models.CharField()
    semester_id = serializers.IntegerField()
    department_id = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'father_name', 'email', 'phone', 'address', 'password', 'semester_id', 'department_id','image']