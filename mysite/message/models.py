from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.
class Message(models.Model):
	"""docstring for Message"""
	sender = models.ForeignKey(User, related_name="sender")
	acceptor = models.ForeignKey(User, related_name="acceptor")
	content = models.CharField(max_length=1000)
	pub_date = models.DateTimeField('date published', default=timezone.now)

	
		
		