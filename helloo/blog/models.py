from django.db import models
from taggit.managers import TaggableManager
from django import forms
from django.contrib import admin

class Post(models.Model):

	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField()
	tags = TaggableManager()
	order = models.CharField(max_length=2)
	picture_name = models.CharField(max_length=60, blank=True)
	ALIGNMENT_CHOICES = (
		('1', 'left'),
		('2', 'right'),
		('3', 'center'),
	)
	SIZE_CHOICES = (
		('1', 'small'),
		('2', 'medium'),
		('3', 'large'),
	)
	PICTURE_CHOICES = (
		('1', 'Include a picture'),
		('2', 'Don\'t include a picture'),
	)
	FILE_TYPE_CHOICES = (
		('gif', '.gif'),
		('jpg', '.jpf'),
		('bmp', '.bmp'),
	)
	include_picture = models.CharField(max_length=1, blank=True, choices=PICTURE_CHOICES)
	alignment = models.CharField(max_length=1, blank=True, choices=ALIGNMENT_CHOICES)
	size = models.CharField(max_length=1, blank=True, choices=SIZE_CHOICES)
	file_type = models.CharField(max_length=3, blank=True, choices=FILE_TYPE_CHOICES)
	#posted_by = user
	
	
	def __unicode__(self):
		return self.title
		
class Picture(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
    	return self.name

class Image(models.Model):
    picture = models.ForeignKey(Picture)
    image = models.ImageField(upload_to='./')
    
    	
class InlineImage(admin.TabularInline):
    model = Image


class PictureAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Picture, PictureAdmin)
