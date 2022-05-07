from msilib import type_binary
from urllib import response
from django.urls import reverse, resolve, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from utils.apiUtils import get_token
import requests
from rest_framework import status


# Create your views here.

# Homepage

class homePage(LoginRequiredMixin, View):
    # redirect_field_name = 'redirect_to'
    template_name = 'home/dash.html'
    dashEndpoint = reverse_lazy('api:dash-list')
    typeEndpoint = reverse_lazy('api:partcategory-list')
    

    
    def get(self,request):

        apiHeader = get_token(user= request.user, asHeader=True)
             
        # Get dash endpoint data
        try:
            dashGet = requests.get(url=request.build_absolute_uri(self.dashEndpoint), headers=apiHeader)
            dashGet.raise_for_status()
            

        except requests.exceptions.HTTPError as e:
            return HttpResponse(content=f"""<h1>Something went wrong</h1>
                                            <h2>CODE: {dashGet.status_code}  {dashGet.reason}</h2>
                                            <h2>{e.response.text}</h2>
                                            """)
        
        # Get types endpoint data
        try:
            typeGet = requests.get(url=request.build_absolute_uri(self.typeEndpoint), headers=apiHeader)
            typeGet.raise_for_status()
            

        except requests.exceptions.HTTPError as e:
            return HttpResponse(content=f"""<h1>Something went wrong</h1>
                                            <h2>CODE: {typeGet.status_code}  {typeGet.reason}</h2>
                                            <h2>{e.response.text}</h2>
                                            """)

        data ={'dash':dashGet.json(), 'types':typeGet.json(), 'module':'Dashboard'}
        
        return render(request, template_name=self.template_name, context=data)




def logoutRedirect(request):
    # print(request)
    logout(request=request)
    
    return HttpResponseRedirect(redirect_to=reverse('home:home'))