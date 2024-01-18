import datetime

from django.db import models
from django.utils import timezone

class  Domain(models.Model):
    domain_url = models.CharField(max_length=200)
    domain_added = models.DateTimeField("The date domain was added to Orbit")

    def __str__(self):
        return self.domain_url