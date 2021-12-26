from django.urls import path
from . import views

app_name = 'SeasonMall'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('prdt_mngm/', views.prdt_mngm, name='prdt_mngm'),
    path('addition/', views.addition, name='addition'),
    path('deletion/', views.deletion, name='deletion'),
]