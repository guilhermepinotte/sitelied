from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the SERVIÇOS index.")