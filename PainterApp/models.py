from django.db import models

# Create your models here.


class Block(models.Model):
    Name = models.CharField(max_length=300, null=True, blank=True)


class MasterPiece(models.Model):
    MasterPiece = models.ImageField(upload_to='Masterpieces')
    Name = models.CharField(max_length=300, null=True, blank=True)
    Block = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, blank=True)

