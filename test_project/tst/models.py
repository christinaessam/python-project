from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=200)

class Post(models.Model):
	title = models.CharField(max_length = 200)
	#pictue = models.ImageField()
	content = models.TextField()
	#post_category= models.ForeignKey(Category)

class Tag(models.Model):
	tag_name = models.CharField(max_length = 200)

class Tag_Posts(models.Model):
	tag_id = models.ForeignKey(Tag)
	post_id = models.ForeignKey(Post)				

class Users(models.Model):
	user_name = models.CharField(max_length = 200, unique=True)
	user_email = models.CharField(max_length = 200, unique=True)
	user_password = models.CharField(max_length = 200)
	#user_type = models.CharField(max_length = 200)
	#user_repassword = models.CharField(max_length = 200)



