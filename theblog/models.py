from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):  
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255, default="BlogForum")
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default='entertainment')
	snippet = models.CharField(max_length=255)
	likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')


	def total_likes(self):
		return self.likes.count()

	def __str__(self):  
		return self.title + ' | ' + str(self.author)

	#def __str__(self):
		#return str(self.post)
		return self.post


	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))
		return reverse('home')


LIKE_CHOICES = (
	('Like', 'Like'),
	('Unlike', 'Unlike')
)

class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

