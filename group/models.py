from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    about = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(default='no_image.jpg', upload_to='group_img')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'groups'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)
        member = GroupPeople(user_id=self.creator_id, group_id=self.id)
        member.save()
        img = Image.open(self.picture.path)
        output_size = (400, 700)
        img.thumbnail(output_size)
        img.save(self.picture.path)

    @property
    def group_comment_count(self):
        return GroupComment.objects.filter(group_id=self.id).count()


class GroupPeople(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'group_peoples'


class GroupComment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'group_comments'
