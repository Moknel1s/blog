from django.db import models

from django.contrib.auth.models import User

class CustomUser(User):
    phone_number = models.CharField(verbose_name='number', max_length=50)

    def __str__(self):
        return self.phone_number
