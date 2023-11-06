from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description= models.TextField()
    def __str__(self):
        return f"Service {self.id} - {self.title}"

class Geography(models.Model):
    is_active = models.BooleanField(_("is active"))
    name = models.CharField(_("name"), max_length=100, null=False)
    code = models.CharField(
        _("code"),
        max_length=10, 
        unique=True, 
        null=True,
        blank=True)
    class Meta:
        abstract = True
    
class State(Geography):
    ...

class City(Geography):
    state = models.ForeignKey(State, related_name="cities", on_delete=models.DO_NOTHING)
    
class Address(models.Model):
    unit_number = models.CharField(max_length=255, blank=True, null=True)
    street_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    postal_code = models.CharField(_("postal code"), max_length=20, blank=True, null = True)