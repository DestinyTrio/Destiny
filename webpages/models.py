from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = RichTextField()
    photo = models.ImageField(upload_to="hero/%Y/%m/%d")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=300, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextField()
    photo = models.ImageField(upload_to="career/%Y/%m/%d")
    skills = models.TextField(max_length=1000)
    responsibility = RichTextField()
    apply = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('careerDetail', args=[self.slug])

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="team/%Y/%m/%d")
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class CareerForm(models.Model):
    first_Name = models.CharField(max_length=255)
    last_Name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    phone_regex = RegexValidator(
        regex=r'^\d{10}$', message="Up to 10 digits allowed.")
    phone_number = models.CharField(max_length=30, validators=[phone_regex])
    email = models.EmailField(max_length=100)
    employment_Type = models.CharField(max_length=128)
    about = models.TextField(max_length=1000)
    qualify = models.TextField(max_length=1000)
    position = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=60)
    pin_code = models.CharField(max_length=60)

    def __str__(self):
        return self.first_Name


class OfficialSocialHandles(models.Model):
    fb = models.CharField(max_length=50)
    insta = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)

    def __str__(self):
        return self.fb


class Testimonal(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="testimonal/%Y/%m/%d")
    position = models.CharField(max_length=255)
    description = RichTextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
