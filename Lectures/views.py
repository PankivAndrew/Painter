from django.shortcuts import render
from Lectures.models import *
from ArtWorks.models import Block
from ArtWorks.models import SubBlock
from ArtWorks.models import SubSubBlock
from django.utils import translation

# Create your views here.


def lectures(request):
    lecture_and_links = [(lecture, list(LectureLink.objects.filter(Lecture=lecture))) for lecture in Lecture.objects.all()]
    block_sub_block = [[block, [[sub_block, list(SubSubBlock.objects.filter(SubBlock=sub_block))]
                                for sub_block in list(SubBlock.objects.filter(Block=block))]] for block in
                       Block.objects.all()]
    return render(request, 'Lectures/lectures.html', {'lecture_and_links': lecture_and_links,
                                                      'block_sub_block': block_sub_block,
                                                      'lang': translation.get_language()})
