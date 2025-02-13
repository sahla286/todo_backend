from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    choice=[
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    status=models.CharField(max_length=20, choices=choice, default='pending')
    due_date=models.DateField()

    def __str__(self):
        return self.title