from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
def getRoutes(request):
	return JsonResponse('Our API', safe=False)