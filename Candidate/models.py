from django.db import models
from django.db.models.signals import pre_save

from Course.utils import unique_slug_generator

from django.core.urlresolvers import reverse

from django.conf import settings

from Student.models import Student

from Position.models import Position

from PartyList.models import PartyList

User = settings.AUTH_USER_MODEL
# Create your models here.


class Candidate(models.Model):
	user 				= models.ForeignKey(User)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	student				= models.ForeignKey('Student.Student', on_delete=models.CASCADE, related_name='Candidate', null=True, blank=True) 
	party_list			= models.ForeignKey('PartyList.PartyList', on_delete=models.CASCADE, related_name='Candidate', null='True', blank=True)
	position 			= models.ForeignKey('Position.Position', on_delete=models.CASCADE, related_name='Candidate', null='True', blank=True)

	votes = models.IntegerField(default=0)

	# def votes_counter(self):
 #         if self.student:
 #             self.votes += 1
	
	def get_data(self):
	 	return self.student

	def get_absolute_url(self):
	 	return reverse('candidate:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
	  	return self.user

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
 		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Candidate)