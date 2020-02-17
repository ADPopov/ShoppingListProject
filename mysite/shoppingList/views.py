from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello!")
# Create your views here.
