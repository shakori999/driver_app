import uuid 

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse  
# Create your models here.

class User(AbstractUser):
    pass

class Trip(models.Model):
    REQUESTED = 'REQUESTED'
    STARTED = 'STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (STARTED, STARTED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )

