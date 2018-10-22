from django.conf.urls import url

from accounts import views
from accounts.views import HomeView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns =[
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
]