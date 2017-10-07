from django.db import models
from django.conf import settings
from Student.models import Student

User = settings.AUTH_USER_MODEL


# Create your models here.

class Candidate(models.Model):
 	user 				= models.ForeignKey(User, on_delete=models.CASCADE)
 	student 			= models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
 	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)

 	# def __str__(self):
 	# 	return self.slug

class Position(models.Model):
	position_name 		= models.CharField(max_length=200)
	candidate			= models.ForeignKey("Candidate", on_delete=models.CASCADE, related_name='Position', null=True, blank=True)

	def __str__(self):
		return self.position_name