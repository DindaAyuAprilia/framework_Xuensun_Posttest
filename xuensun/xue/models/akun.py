from django.db import models
from django.core.validators import EmailValidator

class Akun(models.Model):
    ADMIN = 1
    USERS = 2
    ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (USERS, 'Users'),
    )

    email = models.EmailField(validators=[EmailValidator()], unique=True)
    password = models.CharField(max_length=128) 
    role = models.IntegerField(choices=ROLE_CHOICES) 
    
    def __str__(self):
        return self.email