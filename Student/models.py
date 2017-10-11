from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

from django.core.urlresolvers import reverse

from .validators import validate_gender, validate_year

from django.conf import settings

from Course.models import Course

User = settings.AUTH_USER_MODEL

Year = (
    	('1', '1st year'),
    	('2', '2nd year'),
    	('3', '3rd year'),
    	('4', '4th year'),
    	('5', '5th year'),
    )

class Student(models.Model):
 	user 				= models.ForeignKey(User)
 	First_name			= models.CharField(max_length=120)
 	Last_name			= models.CharField(max_length=120, null=True, blank=True)
 	Middle_name			= models.CharField(max_length=120, null=True, blank=True)
 	
 	gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

 	year 				= models.CharField(max_length=1, choices=Year, blank=True, help_text='Select your year', validators=[validate_year])
 	Gender 				= models.CharField(max_length=1, choices=gender, blank=True, help_text='Select your gender', validators=[validate_gender])
 	age 				= models.IntegerField()
 	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)

 	course 				= models.ForeignKey('Course.Course', on_delete=models.CASCADE, related_name='Student', null=True, blank=True) 

 	def __str__(self):
 		return '%s, %s %s. - %s' % (self.Last_name, self.First_name, self.Middle_name, self.course)

 	def get_absolute_url(self):
 		# return "/student/%s{self.slug}"
 		return reverse('student:edit', kwargs={'slug': self.slug})

 	@property
 	def title(self):
 		return self.First_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Student)