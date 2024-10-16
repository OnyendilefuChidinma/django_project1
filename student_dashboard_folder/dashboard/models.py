from django.db import models

# Create your models here.

class Student(models.Model):
    STATUS_CHOICES = [
        # ('online', 'Online Exam'),
        # ('class', 'Class Exam'),
        # ('missed', 'Missed Exam'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    program = models.CharField(max_length=100)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='online')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    date_joined = models.DateField()
    rating = models.FloatField()

    def __str__(self):
        return self.full_name
    
    
    class Student_Profile(models.Model):
        pass

    class Program(models.Model):
        pass

    class CohortGroup(models.Model):
        pass