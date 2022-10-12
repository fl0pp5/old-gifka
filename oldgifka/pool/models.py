from django.db import models


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    is_published = models.BooleanField(default=False)


class Tag(models.Model):
    title = models.CharField(max_length=120)


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)