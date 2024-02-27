import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse





def index(request):
    return render(request, 'catalog/index.html')