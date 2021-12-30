from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .forms import AdditionForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
def index(request):
  p_list = Product.objects.order_by('-created_date')
  page = request.GET.get('page','1') #페이징 적용
  paginator = Paginator(p_list, 20)
  page_obj = paginator.get_page(page)
  context = {'p_list':page_obj}
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
  context = {'form':form, 'flag':0}
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
    form = AdditionForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('SeasonMall:management')
  else:
    form = AdditionForm(instance=post)
    context = {'form':form}
  return render(request, 'SeasonMall/prdt_form.html', context)