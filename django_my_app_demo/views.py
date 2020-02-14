from django.shortcuts import render

def index(request):
    context = {
        'days': [1,2,3],
    }

    return render(request, 'index.html', context)