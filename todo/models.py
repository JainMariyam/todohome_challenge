from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.title
 
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    description = models.TextField()
    options=(
        ("pending","pending"),
        ("completed","completed")
    )
    status=models.CharField(max_length=20, choices=options, default='pending')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
