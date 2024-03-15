from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.FileField(upload_to="post-images")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'postapp'
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=100, blank=True, null=True)
    msg = models.TextField()
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', null=True, default=None)
    image = models.FileField(upload_to='comment-image', default='comment-image/user.png')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name