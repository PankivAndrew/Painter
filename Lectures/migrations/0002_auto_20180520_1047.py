# Generated by Django 2.0.4 on 2018-05-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lectures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectureimages',
            name='Lecture',
        ),
        migrations.AddField(
            model_name='lecture',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='Lectures'),
        ),
        migrations.DeleteModel(
            name='LectureImages',
        ),
    ]