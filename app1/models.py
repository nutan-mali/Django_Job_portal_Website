from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class jobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    job_title = models.CharField(max_length = 50,null = True)
    about_the_job = models.TextField(null=True)
    shift_and_schedule = models.TextField(null=True)
    employment_type = models.TextField(null=True)
    requirements = models.TextField(null=True)
    responsibilities  = models.TextField(null=True)
    experience = models.TextField(null=True)
    technologies = models.TextField(null=True)
    company_name = models.CharField(max_length = 50, null = True)
    date_posted = models.TextField(max_length = 10, null = True)
    salary = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    location = models.CharField(max_length = 50,null = True)
    education_required = models.CharField(max_length =50,null = True)
    mode_of_working =  models.CharField(max_length = 50,null = True)
    no_of_positions = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    applied_by_users = models.ManyToManyField(User, related_name='applied_jobs', blank=True)

    
    def __str__(self):
        return self.job_title
    
class jobSearch(models.Model):
    job_post = models.ForeignKey(jobPost, on_delete=models.CASCADE,null = True)
    applicant_name = models.CharField(max_length = 50,null = True)
    college_name = models.CharField(max_length = 50, null = True)
    qualification = models.CharField(max_length=10,null = True) 
    certification = models.CharField(max_length=50,null = True)
    resume = models.FileField(upload_to='resumes/', null=True)
    
    def __str__(self):
        return self.applicant_name
    

class Contact(models.Model):
    name = models.CharField(max_length=30 , null=True)
    phone = models.CharField(max_length=15 ,null=True)
    date = models.DateField(default=timezone.now)
    email = models.EmailField(max_length=30,null=True)
    msg = models.CharField(max_length=150 ,null=True)
    
    
    
    def __str__(self):
        return self.name