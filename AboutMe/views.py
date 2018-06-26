from django.shortcuts import render
from ArtWorks.models import Block
from ArtWorks.models import SubBlock
from ArtWorks.models import SubSubBlock
from AboutMe.models import AboutMe
from django.utils import translation


# Create your views here.


def about_me(request):
    about_me = AboutMe.objects.first()
    block_sub_block = [[block, [[sub_block, list(SubSubBlock.objects.filter(SubBlock=sub_block))]
                                for sub_block in list(SubBlock.objects.filter(Block=block))]] for block in
                       Block.objects.all()]
    return render(request, 'About/about.html', {"block_sub_block": block_sub_block,
                                                "lang": translation.get_language(),
                                                "about_me": about_me})
