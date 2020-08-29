from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')