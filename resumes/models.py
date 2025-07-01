from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    position = models.CharField(max_length=255)
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.position}"

class User(AbstractUser):
    ROLE_CHOICES = [
        ('CANDIDATE', 'Кандидат'),
        ('HR', 'HR-менеджер'),
        ('ADMIN', 'Администратор')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CANDIDATE')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"