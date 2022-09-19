
from django.db import models

# Create your models here.

class abousUs(models.Model):
    profile_Image =models.ImageField(upload_to='profile_Image')
    aboutus_1 = models.TextField(max_length=3000,blank=True)
    aboutus_2= models.TextField(max_length=2000,blank=True)
    main_sub_heading= models.TextField(max_length=2000,blank=True)
    
class Skill(models.Model):
    name = models.CharField(max_length=60,blank=True)
    skill_Image =models.ImageField(upload_to='skills')
    def __str__(self):
        return self.name
class service_name(models.Model):
    service_name = models.CharField(max_length=60,blank=True)
    def __str__(self):
        return self.service_name
    
    
class Project(models.Model):
    id=  models.AutoField(primary_key=True)
    Project_name =models.CharField(max_length=300, blank=True)
    video_Link =models.CharField(max_length=300, blank=True)
    code_Link =models.CharField(max_length=300, blank=True)
    content =models.TextField(blank=True)
    def __str__(self):
        return self.Project_name
class Certificate(models.Model):
    id=  models.AutoField(primary_key=True)
    Certificate_name =models.CharField(max_length=300, blank=True)
    Certificate_image =models.ImageField(upload_to='Certificate',blank=True)
    content =models.TextField(blank=True)
    def __str__(self):
        return self.Certificate_name
class Experience(models.Model):
    id=  models.AutoField(primary_key=True)
    Experience_name =models.CharField(max_length=300, blank=True)
    Experience_image =models.ImageField(upload_to='Certificate',blank=True)
    content =models.TextField(blank=True)
    def __str__(self):
        return self.Experience_name
    
class Mycv (models.Model):
    cvDate =  models.CharField(max_length=255)
    cv= models.FileField(upload_to='CV')
    def __str__(self):
        return self.cvDate
class Hiring(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True)
    email =models.EmailField(max_length=255)
    subject  = models.CharField(max_length=255)
    hiring_for = models.CharField(max_length=255)
    message = models.TextField(max_length=25505)
    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True)
    email =models.EmailField(max_length=255)
    subject  = models.CharField(max_length=255)
    message = models.TextField(max_length=25005)
    def __str__(self):
        return self.name
