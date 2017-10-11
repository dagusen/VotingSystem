from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

from django.core.urlresolvers import reverse

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Course(models.Model):
	user 				= models.ForeignKey(User)
	course_name 		= models.CharField(max_length=100)
	description 		= models.TextField(max_length=500, null=True, blank=True)
	
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	#department 			= models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=True, related_name='Course')
	
	def __str__(self):
		return '%s' % (self.course_name, )#self.department)

	def get_absolute_url(self):
		return reverse('course:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.course_name


def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Course)