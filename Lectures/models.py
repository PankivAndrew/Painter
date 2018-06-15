from django.db import models

# Create your models here.


class Lecture(models.Model):
    Img = models.ImageField(upload_to='Lectures', null=True, blank=True)
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EngName = models.CharField(max_length=300, null=True, blank=True)
    UkDescription = models.CharField(max_length=300, null=True, blank=True)
    EngDescription = models.CharField(max_length=300, null=True, blank=True)

    def __repr__(self):
        return self.UkName


# class LectureImages(models.Model):
#
#     Lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
