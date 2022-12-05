from django.db import models


# Create your models here.
class Advocates(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='media/advocates/', blank=True, null=True)
    short_bio = models.TextField(max_length=500, null=True, blank=True)
    long_bio = models.TextField(max_length=1000, null=True, blank=True)
    advocate_years_exp = models.IntegerField()
    company = models.ForeignKey('Companies', on_delete=models.CASCADE, related_name='advocates')
    youtube = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)


class Companies(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='media/companies/', blank=True, null=True)
    summary = models.TextField(max_length=500, null=True, blank=True)
