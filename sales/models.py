from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now

# Create your models here.
class Sales(models.Model):
    name = models.CharField(max_length=255, db_index=True, null=False)
    amount = models.FloatField(blank=False, null=False)
    agent = models.CharField(max_length=140, blank=True, null=False)
    date = models.DateField(default=now)
    description = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default='')   

    class Meta:
        verbose_name_plural = "Sales"
    def __str__(self):
        return self.agent
    # class Meta:
        # ordering = ['-date']

class Agent(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Agents"

    def __str__(self):
        return self.name

class FirmUser(models.Model):
    user = models.OneToOneField(User, null=True, blank='True', on_delete=models.CASCADE)
    firmname = models.CharField(max_length=600, null=False)
    gstin = models.CharField(max_length=100, null=False,  default='')

    def __str__(self):
        return self.user