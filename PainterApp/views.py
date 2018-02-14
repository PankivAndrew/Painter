from django.shortcuts import render

# Create your views here.
from django.utils import translation


def main_page(request):
    if request.method == "POST":
        translation.activate(request.POST.get("lang", ""))
    return render(request, 'MainPage/index.html')
