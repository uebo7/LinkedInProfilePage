from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about_me = models.CharField(max_length=350)
    current_position = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('profile_info', kwargs={'profile_id': self.id})
    
class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    skills = models.CharField(max_length=350)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'I studied at {self.school} to learn {self.skills}'

    def get_absolute_url(self):
        return reverse('education_info', kwargs={'education_id': self.id})

class Experience(models.Model):
    company = models.CharField(max_length=100)
    years = models.IntegerField(default=1)
    Career = models.CharField(max_length=100)
    about = models.CharField(max_length=350)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'I worked at {self.company} for {self.years} years'
    
    def get_absolute_url(self):
        return reverse('experience_info', kwargs={'experience_id': self.id})
       
   
