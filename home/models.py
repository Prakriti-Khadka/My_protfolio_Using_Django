from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=133)
    email = models.CharField(max_length=133)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


