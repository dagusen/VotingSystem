from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.

class Department(models.Model):
	Department_name		= models.CharField(max_length=100)
	Department_code		= models.CharField(max_length=20, null=True)
	College_Dean		= models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.Department_name
		return '%s - %s - %s' % (self.Department_code, self.Department_name, self.College_Dean)

class Course(models.Model):
	course_name 		= models.CharField(max_length=100)
	description 		= models.TextField(max_length=500, null=True, blank=True)
	department 			= models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=True, related_name='Course')
	
	def __str__(self):
		return '%s - %s' % (self.course_name, self.department)

class Student(models.Model):
 	user 				= models.ForeignKey(User)
 	FirstName			= models.CharField(max_length=120)
 	LastName			= models.CharField(max_length=120, null=True, blank=True)
 	MiddleName			= models.CharField(max_length=120, null=True, blank=True)
 	MiddleName			= models.CharField(max_length=120, null=True, blank=True)
 	
 	gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

 	Gender 				= models.CharField(max_length=1, choices=gender, blank=True, help_text='Select your gender')
 	age 				= models.IntegerField()
 	birthday 			= models.DateTimeField()
 	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)

 	course 				= models.ForeignKey("Course", on_delete=models.CASCADE, related_name='Student', null=True, blank=True)
 	
 	def __str__(self):
 		return '%s, %s %s. - %s' % (self.LastName, self.FirstName, self.MiddleName, self.course)

class Candidate(models.Model):
 	user 				= models.ForeignKey(User, on_delete=models.CASCADE)
 	student 			= models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
 	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)
 	# def __str__(self):
 	# 	return self.user
