# Generated by Django 2.0.4 on 2018-06-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lectures', '0003_lecturelink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='EngDescription',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='EngName',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='UkDescription',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='UkName',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
