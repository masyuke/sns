from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 

# Create your models here.
class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default='a')
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=SnsModel, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Likes(models.Model):
    articles = models.ForeignKey('SnsModel', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'), ('complete', 'primary'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.title



