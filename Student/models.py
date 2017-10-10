from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

from django.core.urlresolvers import reverse

from .validators import validate_gender, validate_year

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Department(models.Model):
	user 				= models.ForeignKey(User)
	Department_name		= models.CharField(max_length=100)
	Department_code		= models.CharField(max_length=20, null=True)
	College_Dean		= models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return '%s - %s - %s' % (self.Department_code, self.Department_name, self.College_Dean)

class Course(models.Model):
	user 				= models.ForeignKey(User)
	course_name 		= models.CharField(max_length=100)
	description 		= models.TextField(max_length=500, null=True, blank=True)
	
	Year = (
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
        ('5', '5th Year'),
    )
	year 				= models.CharField(max_length=1, choices=Year, blank=True, help_text='Select your year', validators=[validate_year])
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	department 			= models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=True, related_name='Course')
	
	def __str__(self):
		return '%s - %s' % (self.course_name, self.department)

class Student(models.Model):
 	user 				= models.ForeignKey(User)
 	First_name			= models.CharField(max_length=120)
 	Last_name			= models.CharField(max_length=120, null=True, blank=True)
 	Middle_name			= models.CharField(max_length=120, null=True, blank=True)
 	
 	gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

 	Gender 				= models.CharField(max_length=1, choices=gender, blank=True, help_text='Select your gender', validators=[validate_gender])
 	age 				= models.IntegerField()
 	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)

 	course 				= models.ForeignKey("Course", on_delete=models.CASCADE, related_name='Student', null=True, blank=True)
 	
 	def __str__(self):
 		return '%s, %s %s. - %s' % (self.Last_name, self.First_name, self.Middle_name, self.course)

 	def get_absolute_url(self):
 		#return "/student/%s{self.slug}"
 		return reverse('student:edit', kwargs={'slug': self.slug})

 	@property
 	def title(self):
 		return self.FirstName

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Student)