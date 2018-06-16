from django.db import models

# Create your models here.


class Lecture(models.Model):
    Img = models.ImageField(upload_to='Lectures', null=True, blank=True)
    UkName = models.CharField(max_length=1000, null=True, blank=True)
    EngName = models.CharField(max_length=1000, null=True, blank=True)
    UkDescription = models.CharField(max_length=3000, null=True, blank=True)
    EngDescription = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return "Lecture: " + self.UkName


class LectureLink(models.Model):
    Link = models.URLField()
    Lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Lecture.UkName

# class LectureImages(models.Model):
#
#     Lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
