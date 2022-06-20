from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.core import serializers
from .serializer import *
from rest_framework import generics, status
from django.http import HttpResponse


# Create your views here.
class SectionCreateView(generics.ListCreateAPIView):
    queryset = Section.objects.filter(is_deleted=False)
    serializer_class = SectionSerializer
    permission_classes = [AllowAny]


class SectionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.filter(is_deleted=False)
    serializer_class = SectionSerializer
    permission_classes = [AllowAny]


class SemesterCreateView(generics.ListCreateAPIView):
    queryset = Semester.objects.filter(is_deleted=False)
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            section = Section.objects.filter(section_no=request.data['section_id'], is_deleted=False)[0]
            course = Course.objects.filter(pk=request.data['course_id'], is_deleted=False)[0]
            user_key = Semester.objects.create(semester=request.data['semester'], start_date=request.data['start_date'], end_date=request.data['end_date'], section_id=section, course_id=course)
            return Response({'message': 'Created Successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            query_set = Semester.objects.filter(is_deleted=False)
            if query_set.exists():
                # semester_detail = query_set.values('id', 'semester', 'start_date', 'end_date', 'section_id',
                #                                    'course_id')
                objects = Semester.objects.filter(is_deleted=False)
                list =[]
                #
                # course = Course.objects.filter(pk=request.data['course_id'], is_deleted=False)[0]
                for _ in objects:
                    # section = Section.objects.filter(section_no=_.section_id, is_deleted=False)[0]
                    # course = Course.objects.filter(pk=_.course_id.id, is_deleted=False)[0]
                    ctx = {'id': _.id,
                           'semester': _.semester,
                           'start_date': _.start_date,
                           'end_date': _.end_date,
                           'section_id': _.section_id.id,
                           'course_id': _.course_id.instance.id}
                    list.append(ctx)
                return Response(list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SemesterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.filter(is_deleted=False)
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk, *args, **kwargs):
        try:
            query_set = Semester.objects.filter(pk=pk, is_deleted=False)
            if query_set.exists():
                semester_detail = query_set.values('id', 'semester', 'start_date', 'end_date', 'section_id', 'course_id')
                # section = Section.objects.filter(section_no=request.data['section_id'], is_deleted=False)[0]
                # course = Course.objects.filter(pk=request.data['course_id'], is_deleted=False)[0]
                ctx = {'id': semester_detail[0]["id"],
                       'semester' : semester_detail[0]["semester"],
                       'start_date' : semester_detail[0]["start_date"],
                       'end_date' : semester_detail[0]["end_date"],
                       'section_id' : semester_detail[0]["section_id"],
                       'course_id' : semester_detail[0]["course_id"]}
                return Response(ctx, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CourseCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.filter(is_deleted=False)
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.filter(is_deleted=False)
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class DepartmentCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.filter(is_deleted=False)
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]


class DepartmentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.filter(is_deleted=False)
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]


class StudentCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            semester = Semester.objects.filter(pk=request.data['semester_id'], is_deleted=False)[0]
            department = Department.objects.filter(pk=request.data['department_id'], is_deleted=False)[0]
            file = request.FILES['image']
            Student.objects.create(first_name=request.data['first_name'],
                                   last_name=request.data['last_name'],
                                   father_name=request.data['father_name'],
                                   email=request.data['email'],
                                   phone=request.data['phone'],
                                   address=request.data['address'],
                                   password=request.data['password'],
                                   semester_id=semester,
                                   department_id=department,
                                   image=file)
            return Response({'message': 'Created Successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            query_set = Student.objects.filter(is_deleted=False)
            if query_set.exists():
                objects = Student.objects.filter(is_deleted=False)
                list = []
                for _ in objects:
                    ctx = {'id': _.id,
                           'first_name': _.first_name,
                           'last_name': _.last_name,
                           'father_name': _.father_name,
                           'email':  _.email,
                           'phone': _.phone,
                           'address': _.address,
                           'password': _.password,
                           'semester_id': _.semester_id.semester,
                           'department_id': _.department_id.dept_name,
                           'image': _.image.url
                           }
                    list.append(ctx)
                return Response(list, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk, *args, **kwargs):
        try:
            query_set = Student.objects.filter(pk=pk, is_deleted=False)
            if query_set.exists():
                semester_detail = query_set.values('id', 'first_name', 'last_name', 'father_name', 'email', 'phone', 'address', 'password', 'semester_id', 'department_id', 'image')
                # section = Section.objects.filter(section_no=request.data['section_id'], is_deleted=False)[0]
                # course = Course.objects.filter(pk=request.data['course_id'], is_deleted=False)[0]
                ctx = {'id': semester_detail[0]["id"],
                       'first_name': semester_detail[0]["first_name"],
                       'last_name': semester_detail[0]["last_name"],
                       'father_name': semester_detail[0]["father_name"],
                       'email': semester_detail[0]["email"],
                       'phone': semester_detail[0]["phone"],
                       'address': semester_detail[0]["address"],
                       'password': semester_detail[0]["password"],
                       'semester_id': semester_detail[0]["semester_id"],
                       'department_id': semester_detail[0]["department_id"],
                       'image': semester_detail[0]["image"]}
                return Response(ctx, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)