from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User   #user-post relation is one to many
from django.urls import reverse

class Post(models.Model):
	title=models.CharField(max_length=100) #in post table->title fiels is created
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)  
	#(auto_now=True) can be passed in DateTime field-->current date-time
	#(auto_now_add=True) can be passed in DateTime field-->date-time when the object was created -->we wont use either-->we want to change the date when we want it to.
	
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	#it is foreign key as one to many relation is there b/w user and post.
	#on_delete= used when the user gets deleted, models.CASCADE enable the post to be deleted too when the user gets deleted.

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
	post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
	name=models.CharField(max_length=255)
	body=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title,self.name)
	
		
		





