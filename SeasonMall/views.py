from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .forms import AdditionForm
from .models import User, Product
# Create your views here.
def index(request):
  product_list = Product.objects.order_by('-created_date')
  context = {'product_list':product_list}
  return render(request, 'SeasonMall/index.html', context)

def prdt_mngm(request):
  return render(request, 'SeasonMall/prdt_mngm.html')

def addition(request): #POST
  if request.method == 'POST':
    form = AdditionForm(request.POST)
    if form.is_valid(): #if valid
      product = form.save(commit=False)
      product.created_date = timezone.now()
      #판매자 정보
      #이미지 정보
      product.save()
      return redirect('SeasonMall:index')
  else: #GET
    form = AdditionForm()
  context = {'form':form}
  return render(request, 'SeasonMall/prdt_form.html', context)

def deletion(request):