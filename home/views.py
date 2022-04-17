from urllib import response
from django.urls import reverse, resolve
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

# Homepage

class homePage(LoginRequiredMixin, View):
    # redirect_field_name = 'redirect_to'
    template_name = 'home/home.html'
    
    def get(self,request):
        return render(request, template_name=self.template_name)


def logoutRedirect(request):
    print(request)
    logout(request=request)
    
    return HttpResponseRedirect(redirect_to=reverse('home:home'))