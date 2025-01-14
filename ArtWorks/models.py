from django.db import models


class Block(models.Model):
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EnName = models.CharField(max_length=300, null=True, blank=True)
    Block_URL = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.UkName


class SubBlock(models.Model):
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EnName = models.CharField(max_length=300, null=True, blank=True)
    Block = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.UkName


class SubSubBlock(models.Model):
    UkName = models.CharField(max_length=300, null=True, blank=True)
    EnName = models.CharField(max_length=300, null=True, blank=True)
    SubBlock = models.ForeignKey(SubBlock, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.UkName


class MasterPiece(models.Model):
    MasterPiece = models.ImageField(upload_to="Masterpieces")
    UkName = models.CharField(max_length=300, default=None)
    EnName = models.CharField(max_length=300, null=True, blank=True)
    UkDescription = models.TextField(blank=True, null=True)
    EnDescription = models.TextField(blank=True, null=True)
    SubBlock = models.ForeignKey(SubBlock, on_delete=models.CASCADE, null=True, blank=True)
    SubSubBlock = models.ForeignKey(SubSubBlock, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.UkName
