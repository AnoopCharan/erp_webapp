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
        dashGet = requests.get(url=request.build_absolute_uri(self.dashEndpoint), headers=apiHeader)
        dashData = dashGet.json()
        typeGet = requests.get(url=request.build_absolute_uri(self.typeEndpoint), headers=apiHeader)
        typeData = typeGet.json()

        data ={'dash':dashData, 'types':typeData, 'module':'Dashboard'}
        return render(request, template_name=self.template_name, context=data)

        try:
            dashGet = requests.get(url=request.build_absolute_uri(self.dashEndpoint), headers=apiHeader)
            dashData = dashGet.json()
            typeGet = requests.get(url=request.build_absolute_uri(self.typeEndpoint), headers=apiHeader)
            typeData = typeGet.json()

            data ={'dash':dashData, 'type':typeData}
            return render(request, template_name=self.template_name, context=data)

        except:
            return HttpResponse(content=f"""<h1>{dashGet.request} : RESPONSE {dashGet.status_code}, {dashGet.reason} </h1>
                                            <h1>{typeGet.request} : RESPONSE {typeGet.status_code}, {typeGet.reason} </h1>""")
        



def logoutRedirect(request):
    print(request)
    logout(request=request)
    
    return HttpResponseRedirect(redirect_to=reverse('home:home'))