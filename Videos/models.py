from django.db import models

# Create your models here.


class Video(models.Model):
    Name = models.CharField(max_length=300, null=False, blank=False)
    Video = models.FileField(upload_to='Video', null=False, blank=False)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name
