from django.contrib.gis.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	image = models.ImageField(upload_to="post_image", null=True)
	author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True) 
	create_at = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

class Author (models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	image = models.ImageField(upload_to="author_image")
	create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	update_at = models.DateTimeField(auto_now=False, auto_now_add=True)