from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name = 'common/login.html'), name='login'), #default는 registration/login.html인데 common에 만들 것이기 때문에 괄호에 설정해준 경우임
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup, name='signup'),
]