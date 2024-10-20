from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # Import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # Store videos in Cloudinary
    video = CloudinaryField('video', blank=True, null=True)  # Replace FileField
    
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Store images in Cloudinary
    image = CloudinaryField('image', blank=True, null=True)  # Replace ImageField

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
