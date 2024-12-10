from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_image') 
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Add related_name argument to avoid clashes with reverse accessor for auth.User.groups
    groups = models.ManyToManyField(
        to='auth.Group',
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_set',
    )

    # Add related_name argument to avoid clashes with reverse accessor for auth.User.user_permissions
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_user_set',
    )

    def __str__(self):
        return self.username
    
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}: {self.subject}"