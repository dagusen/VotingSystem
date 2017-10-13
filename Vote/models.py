from django.db import models

# Create your models here.

from django.conf import settings

from Candidate.models import Candidate

User = settings.AUTH_USER_MODEL

class Law(models.Model):
	yes_vote		= models.IntegerField(default=0)
	no_vote			= models.IntegerField(default=0)

class Voter(models.Model):
	user 			= models.ForeignKey(User)
	#candidate 		= models.ForeignKey(Candidate)
	law 			= models.ForeignKey(Law)	
	#timestamp		= models.DateTimeField(auto_now_add=True)