from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
	tag_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.tag_name
	
class Category(models.Model):
	category_name = models.CharField(max_length=200)
	def __str__(self):
		return self.category_name

class Post (models.Model):
	title = models.CharField(max_length = 200)
	post_content = RichTextUploadingField()
	author = models.ForeignKey(User)
	post_category= models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag)
	date=models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.title
	

