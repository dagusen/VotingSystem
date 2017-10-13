from django.db import models

# Create your models here.

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Law(models.Model):
	yes_vote		= models.IntegerField(default=0)
	no_vote			= models.IntegerField(default=0)

class Voter(models.Model):
	user 			= models.ForeignKey(User)
	law 			= models.ForeignKey(Law)

	