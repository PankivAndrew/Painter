from django.shortcuts import render
from ArtWorks.models import Block
from ArtWorks.models import MasterPiece

# Create your views here.
from django.utils import translation


def main_page(request):
    masterpieces = MasterPiece.objects.all()
    blocks = Block.objects.all()
    return render(request, 'MainPage/index.html', {"masterpieces": masterpieces,
                                                   "blocks": blocks,
                                                   "lang": translation.get_language()})


def about(request):
    print(translation.get_language())
    return render(request, 'About/about.html')


def header(request):
    blocks = Block.objects.all()
    print("blocks", blocks)
    render(request, 'layouts/header.html', {"blocks": blocks, "lang": translation.get_language()})

