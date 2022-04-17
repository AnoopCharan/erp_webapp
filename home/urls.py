from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from home.views import homePage, logoutRedirect


app_name = 'home'

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('logout', logoutRedirect, name='logoutRedirect'),
    path('test',(TemplateView.as_view(template_name='registration/login_test.html')), name='test')
]