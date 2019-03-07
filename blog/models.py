from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Post like model
class PostLike(models.Model):
    post_id = models.IntegerField(null=True, blank=True)
    like = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)


# Create Post models.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    like = models.OneToOneField(PostLike, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @property
    def like_count(self):
        if self.like is None:
            return 0
        return self.like.like
