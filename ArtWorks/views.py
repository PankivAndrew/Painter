from django.shortcuts import render

# Create your views here.
from django.utils import translation


def main_page(request):
    print(translation.get_language())
    return render(request, 'MainPage/index.html')


def about(request):
    print(translation.get_language())
    return render(request, 'About/about.html')
