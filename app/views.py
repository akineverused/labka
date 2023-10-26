from django.shortcuts import render


def home(request):
    content = {
        'name': "MADI'S PROJECT"
    }

    return render(request, 'base.html', content)
