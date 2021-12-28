from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import AdditionForm
from .models import User, Product
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
  p_list = Product.objects.order_by('-created_date')
  context = {'p_list':p_list}
  return render(request, 'SeasonMall/index.html', context)

def prdt_mngm(request):
  return render(request, 'SeasonMall/prdt_mngm.html')

#@login_required(login_url='common:login')
def addition(request): #POST
  if request.method == 'POST':
    form = AdditionForm(request.POST)
    if form.is_valid(): #if valid
      product = form.save(commit=False)
      product.created_date = timezone.now()
      product.author = request.user
      #판매자 정보
      #이미지 정보
      product.save()
      return redirect('SeasonMall:index')
  else: #GET
    form = AdditionForm()
  context = {'form':form}
  return render(request, 'SeasonMall/prdt_form.html', context)


def management(request):
  p_list = Product.objects.order_by('-created_date')
  context = {'p_list':p_list}
  return render(request, 'SeasonMall/management.html/', context)
