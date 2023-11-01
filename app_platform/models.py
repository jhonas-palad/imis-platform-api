from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description= models.TextField()
    def __str__(self):
        return f"Service {self.id} - {self.title}"

class Address(models.Model):
    unit_number = models.CharField(max_length=255, blank=True, null=True)
    street_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    postal_code = models.CharField(max_length=20, blank=False, null=False)