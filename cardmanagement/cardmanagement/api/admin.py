from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Department)
admin.site.register(Student)