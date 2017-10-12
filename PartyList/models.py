from django.db import models
from django.db.models.signals import pre_save

from Course.utils import unique_slug_generator

from django.core.urlresolvers import reverse

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class PartyList(models.Model):
	user 				= models.ForeignKey(User)
	partylist_name		= models.CharField(max_length=150)
	goals				= models.CharField(max_length=150, null=True, blank=True)
	projects			= models.CharField(max_length=150, null=True, blank=True)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)
	
	def __str__(self):
		return self.partylist_name

	def get_absolute_url(self):
	 	return reverse('partylist:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
	 	return self.partylist_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=PartyList)