
from urllib import response
from django.urls import reverse, resolve, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from utils.apiUtils import api_get, api_auth
import requests
from rest_framework import status


# Create your views here.



# Homepage

class HomePage(LoginRequiredMixin, View):
    # redirect_field_name = 'redirect_to'
    template_name = 'home/dash.html'
    dashEndpoint = reverse_lazy('api:dash-list')
    typeEndpoint = reverse_lazy('api:partcategory-list')

    def get(self,request):

        dashUrl = request.build_absolute_uri(self.dashEndpoint)
        dashGet = api_get(url= dashUrl, request= request)
        print(dashGet.status_code)

        typeUrl = request.build_absolute_uri(self.typeEndpoint)
        typeGet = api_get(url=typeUrl, request=request)

        data ={'dash':dashGet.json(), 'types':typeGet.json(), 'module':'Dashboard'}
        
        return render(request, template_name=self.template_name, context=data)

class CurrentStock(LoginRequiredMixin, View):
    template_name = 'current/current.html'
    dashEndpoint = reverse_lazy('api:dash-list')
    typeEndpoint = reverse_lazy('api:partcategory-list')

    def get(self,request):

        dashUrl = request.build_absolute_uri(self.dashEndpoint)
        dashGet = api_get(url= dashUrl, request= request)
        print(dashGet.status_code)

        typeUrl = request.build_absolute_uri(self.typeEndpoint)
        typeGet = api_get(url=typeUrl, request=request)

        data ={'dash':dashGet.json(), 'types':typeGet.json(), 'module':'Current Stock'}
        
        return render(request, template_name=self.template_name, context=data)

class MinimumStock(LoginRequiredMixin, View):
    template_name = 'min/min.html'
    dashEndpoint = reverse_lazy('api:dash-list')
    typeEndpoint = reverse_lazy('api:partcategory-list')

    def get(self,request):

        dashUrl = request.build_absolute_uri(self.dashEndpoint)
        dashGet = api_get(url= dashUrl, request= request)
        print(dashGet.status_code)

        typeUrl = request.build_absolute_uri(self.typeEndpoint)
        typeGet = api_get(url=typeUrl, request=request)


        data ={'dash':dashGet.json(), 'types':typeGet.json(), 'module':'Minimum Stock'}
        
        return render(request, template_name=self.template_name, context=data)


def logoutRedirect(request):
    # print(request)
    logout(request=request)
    
    return HttpResponseRedirect(redirect_to=reverse('frontend:home'))