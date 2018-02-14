from django.db import models


class Block(models.Model):
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EnName = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.UkName


class MasterPiece(models.Model):
    MasterPiece = models.ImageField(upload_to="Masterpieces")
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EnName = models.CharField(max_length=300, null=True, blank=True)
    UkDescription = models.TextField(blank=True, null=True)
    EnDescription = models.TextField(blank=True, null=True)
    Block = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.UkName
