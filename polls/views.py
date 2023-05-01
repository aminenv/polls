from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')

def index(request):
    context = {}
    return render(request, 'index.html', context)

# Create your views here.
