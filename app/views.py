from django.shortcuts import render
from .models import Students

def home(request):
    info = Students.objects.all()

    a = []
    for x in info:
        a.append(x)

    content = {
        'sdu': a,
        'title': "myproject"
    }

    return render(request, 'base.html', content)
