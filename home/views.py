from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.utils.html import format_html

# Create your views here

def credits(request):
    content = "YES"

    return HttpResponse(content, content_type="text/plain")


def news(request):
    data = {
        'news': [
            "Good news all the time",
            "Good news first time",
        ]
    }

    return render(request, 'news.html', data)


def temp(request):
    data = {"instrument": f"{format_html('<em>{}</em>', 'Tuba > Baritone')}"}
    return render(request, 'temp.html', data)