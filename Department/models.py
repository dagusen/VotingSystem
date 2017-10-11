from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

from django.core.urlresolvers import reverse

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Department(models.Model):
	user 				= models.ForeignKey(User)
	department_name		= models.CharField(max_length=100)
	department_code		= models.CharField(max_length=20, null=True)
	college_dean		= models.CharField(max_length=120, null=True, blank=True)

	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)
	
	def __str__(self):
		return '%s - %s - %s' % (self.department_code, self.department_name, self.college_dean)

	def get_absolute_url(self):
		return reverse('department:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
	 	return self.department_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Department)