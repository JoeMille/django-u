from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'catalog/base.html')

def index(request):
    return render(request, 'catalog/index.html')
