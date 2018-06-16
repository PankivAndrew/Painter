from django.shortcuts import render
from Lectures.models import *
from ArtWorks.models import Block
from django.utils import translation

# Create your views here.


def lectures(request):
    lecture_and_links = [(lecture, list(LectureLink.objects.filter(Lecture=lecture))) for lecture in Lecture.objects.all()]
    blocks = Block.objects.all()
    return render(request, 'Lectures/lectures.html', {'lecture_and_links': lecture_and_links,
                                                      "blocks": blocks,
                                                      'lang': translation.get_language()})
