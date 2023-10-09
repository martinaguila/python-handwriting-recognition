from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def hi(request):
    return render(request, 'appwebsite/home.html')

def my_view(request):
    if request.method == 'GET':
        message = "Hello, World!"
        return JsonResponse({'message': message})