from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_provider = models.BooleanField('Is provider', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Provider(models.Model):
    user=models.OneToOneField(User, related_name="freelancer", on_delete=models.CASCADE)
    ruc=models.IntegerField(verbose_name="Ruc")
    phone=models.IntegerField(verbose_name="Teléfono", null=True, blank=True)
    skills=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    portofolio=models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.user.username



class Client(models.Model):
    user=models.OneToOneField(User, related_name="employer", on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.company_name