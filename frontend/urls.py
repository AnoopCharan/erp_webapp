from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from frontend import views


app_name = 'frontend'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('current', views.CurrentStock.as_view(), name='currentHome'),
    path('min', views.MinimumStock.as_view(), name='minHome'),
    path('logout', views.logoutRedirect, name='logoutRedirect'),
    path('test',(TemplateView.as_view(template_name='registration/login_test.html')), name='test')
]