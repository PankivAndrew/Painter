from django.db import models

# Create your models here.


class AboutMe(models.Model):
    UkText = models.TextField(null=False, blank=False)
    EngText = models.TextField(null=True, blank=True)
