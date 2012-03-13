from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):

	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField()
	tags = TaggableManager()
	#order = models.CharField(max_length=2)
	#posted_by = user
	
	
	
	def __unicode__(self):
		return self.title
