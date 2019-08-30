from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Companies(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    motto = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(default='no_image.jpg', upload_to='company_img')

    class Meta:
        db_table = 'companies'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Companies, self).save(*args, **kwargs)
        img = Image.open(self.picture.path)
        output_size = (400, 700)
        img.thumbnail(output_size)
        img.save(self.picture.path)
