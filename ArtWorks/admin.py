from django.contrib import admin
from .models import SubBlock, MasterPiece, Block, SubSubBlock

# Register your models here.
admin.site.register(SubBlock)
admin.site.register(MasterPiece)
admin.site.register(Block)
admin.site.register(SubSubBlock)
