from django.shortcuts import render
from Lectures.models import *
from ArtWorks.models import Block
from django.utils import translation

# Create your views here.


def lectures(request):
    lectures = Lecture.objects.all()
    blocks = Block.objects.all()
    return render(request, 'Lectures/index.html', {'lectures': lectures,
                                                   "blocks": blocks,
                                                   "lang": translation.get_language()})
