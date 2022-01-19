from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'SeasonMall'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('prdt_mngm/', views.prdt_mngm, name='prdt_mngm'),
    path('addition/', views.addition, name='addition'),
    path('management/', views.management, name='management'),
    path('prdt_delete/<int:product_id>/', views.prdt_delete, name='prdt_delete'),
    path('prdt_modify/<int:product_id>/', views.prdt_modify, name='prdt_modify'),
    path('prdt_info/<int:product_id>/', views.prdt_info, name = 'prdt_info'),
    path('like/<int:product_id>/', views.product_like, name="product_like"),
]