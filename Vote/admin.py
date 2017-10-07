from django.contrib import admin
from .models import (
	Department, 
	Course, 
	Student, 
	Candidate,
	)
# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Candidate)