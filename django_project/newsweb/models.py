from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=200)

class Post (models.Model):
	title = models.CharField(max_length = 200)
	post_content = RichTextUploadingField()
	author = models.ForeignKey(User)
	post_category= models.ForeignKey(Category)
	#post_image= models.ImageField(upload_to='python_project/django_project/images')
	date=models.DateTimeField(default=datetime.now)
class Tag(models.Model):
	tag_name = models.CharField(max_length = 200)

class Tag_Posts(models.Model):
	tag_id = models.ForeignKey(Tag)
	post_id = models.ForeignKey(Post)		

