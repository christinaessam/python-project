from django.contrib import admin
from .models import Category,Post,Tag,Tag_Posts
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Tag_Posts)
