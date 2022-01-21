from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import AdditionForm
from .models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
import stripe
from django.conf import settings
from django.db.models import Q
import json

User = get_user_model()
# Create your views here.
def index(request):
  p_list = Product.objects.order_by('-created_date')
  kw = request.GET.get('kw', '')
  if kw:
    p_list = p_list.filter(Q(name__icontains=kw))

  page = request.GET.get('page','1') #페이징 적용
  paginator = Paginator(p_list, 16)
  page_obj = paginator.get_page(page)
  context = {'p_list':page_obj, 'page':page, 'kw':kw}
  return render(request, 'SeasonMall/index.html', context)

def prdt_mngm(request):
  return render(request, 'SeasonMall/prdt_mngm.html')

#@login_required(login_url='common:login')
def addition(request): #POST
  if request.method == 'POST':
    form = AdditionForm(request.POST, request.FILES) #POST한 내용을 queryset으로 이동
    if form.is_valid(): #if valid
      product = form.save(commit=False)
      product.created_date = timezone.now()
      product.author = request.user
      product.save()
      return redirect('SeasonMall:index')
  else: #GET
    form = AdditionForm()
  context = {'form':form}
  return render(request, 'SeasonMall/prdt_form.html', context)


def management(request):
  p_list = Product.objects.filter(author_id=request.user)  
  p_list = p_list.order_by('-created_date')
  context = {'p_list':p_list}
  return render(request, 'SeasonMall/management.html/', context)

def prdt_delete(request, product_id):
  post = get_object_or_404(Product, pk=product_id)
  if request.method == 'POST':
    post.delete()
    return redirect('SeasonMall:management')
  else:
    context = {'post':post} #?
  return render(request, 'SeasonMall/prdt_delete.html', context)

def prdt_modify(request, product_id):
  post = get_object_or_404(Product, pk=product_id)
  if request.method == 'POST':
    form = AdditionForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return redirect('SeasonMall:management')
  else:
    form = AdditionForm(instance=post)
    context = {'form':form}
  return render(request, 'SeasonMall/prdt_form.html', context)

def prdt_info(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  if request.method == 'POST':
    context = {'prod':product}
    return render(request, 'SeasonMall/prdt_info.html', context)
  else:
    context = {'product':product}
  return render(request, 'SeasonMall/prdt_info.html', context)


@login_required(login_url='common:login')
def product_like(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  user = request.user
  
  if user in product.like.all():
    product.like.remove(user)
    product.like_count -= 1
    product.save()
  else:
    product.like.add(user)
    product.like_count += 1
    product.save()
  return redirect('SeasonMall:prdt_info', product_id=product.id)
  # return HttpResponse(json.dumps(context), content_type='application/json')
  #json.dumps --> json의 사전으로 만듦
  
def myprofile(request):
  me = request.user
  context = {'me':me}
  return render(request, 'SeasonMall/myprofile.html', context)