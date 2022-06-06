from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Base model which extends in all models to inherit common fields.
    """
    is_deleted = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()


class Section(BaseModel):
    """
    Section Table
    """
    section_no = models.CharField(max_length=200)
    section_year = models.CharField(max_length=200)

    class Meta:
        db_table = 'section'
        verbose_name = 'section'
        verbose_name_plural = 'sections'

    def __str__(self):
        return self.section_no


class Course(BaseModel):
    """
    Course Table
    """
    course_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'course'
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.course_name


class Semester(BaseModel):
    """
    Semester Table
    """
    semester = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, related_name='section_id')
    course_id = models.ManyToManyField(Course, null=True, related_name='course_id')

    class Meta:
        db_table = 'semester'
        verbose_name = 'semester'
        verbose_name_plural = 'semesters'

    def __str__(self):
        return self.semester


class Department(BaseModel):
    """
    Department Table
    """
    dept_name = models.CharField(max_length=200)
    dept_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    class Meta:
        db_table = 'department'
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.dept_name


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.first_name), filename])


class Student(BaseModel):
    """
    Student Table
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=500, null=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, related_name='semester_id')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name='department_id')
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return self.first_name



