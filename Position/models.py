from django.db import models
from django.db.models.signals import pre_save

from Course.utils import unique_slug_generator

from django.core.urlresolvers import reverse

from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.


class Position(models.Model):
	user 				= models.ForeignKey(User)
	position_name 		= models.CharField(max_length=200)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.position_name

	def get_absolute_url(self):
	  	return reverse('position:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
	 	return self.position_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Position)