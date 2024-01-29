from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()


class Authors(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    