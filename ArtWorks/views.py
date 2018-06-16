from django.shortcuts import render
from ArtWorks.models import Block
from ArtWorks.models import MasterPiece
from ArtWorks.models import SubBlock
from ArtWorks.models import SubSubBlock

# Create your views here.
from django.utils import translation


def main_page(request):
    masterpieces = MasterPiece.objects.all()
    block_sub_block = [[block, [[sub_block, list(SubSubBlock.objects.filter(SubBlock=sub_block))]
                                for sub_block in list(SubBlock.objects.filter(Block=block))]] for block in
                       Block.objects.all()]
    return render(request, 'MainPage/index.html', {"masterpieces": masterpieces,
                                                   "block_sub_block": block_sub_block,
                                                   "lang": translation.get_language()})


def about(request):
    print(translation.get_language())
    return render(request, 'About/about.html')

