from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  msg = 'hi'
  return render(request, 'SeasonMall/index.html', {'message':msg})

def prdt_mngm(request):
  return render(request, 'SeasonMall/prdt_mngm.html')