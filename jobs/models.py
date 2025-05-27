from django.db import models

class Job(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, default='USD')
    positions = models.IntegerField()
    category = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    requirements = models.JSONField(default=list)
    benefits = models.JSONField(default=list)
    posted_date = models.DateField()
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Application(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    interested_jobs = models.JSONField(default=list)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    inquiry_type = models.CharField(max_length=50, default='job_inquiry')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"