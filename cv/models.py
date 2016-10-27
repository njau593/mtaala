from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Images(models.Model):
    pics = models.ImageField(null=False, blank=False)

class Files(models.Model):
    document = models.FileField(null=False, blank=False)

class About(models.Model):
    description = models.TextField()
    resume = RichTextField()
    profile_Pic = models.ImageField(null=True, blank=False)
    cv = models.FileField(null=True)

class Contact(models.Model):
    reach = RichTextField()

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    extract = models.TextField()
    image = models.ImageField()
    article = RichTextField()
    date = models.DateField(null=True)
