from turtle import pos
from utils.utils import csvread
import json
from django.urls import reverse, resolve, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from utils.apiUtils import api_get, api_auth, api_post



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

        if isinstance(dashGet, HttpResponse):
            return dashGet
        if isinstance(typeGet, HttpResponse):
            return typeGet


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

        if isinstance(dashGet, HttpResponse):
            return dashGet
        if isinstance(typeGet, HttpResponse):
            return typeGet

       

        data ={
            'dash':dashGet.json(),
            'types':typeGet.json(),
            'module':'Current Stock'}
        
        return render(request, template_name=self.template_name, context=data)

class CurrentStockUpdate(LoginRequiredMixin, View):

    def get(self,request):
        return redirect(to=reverse_lazy('frontend:currentHome'))

    def post(self,request):

        partUrl = request.build_absolute_uri(reverse_lazy('api:part-list'))
        partGet = api_get(url= partUrl, request= request)
        partData = partGet.json()

        updateQuantity = request.POST.getlist('new_quantity')

        apiPostData = []

        for count,val in enumerate(updateQuantity):
            if val != "":
                apiPostData.append({
                    'part': partData[count]['url'],
                    'currentStock': int(val)
                })

        currentStockUrl = request.build_absolute_uri(reverse_lazy('api:currentstock-list'))

        apiPost =api_post(
            url= currentStockUrl,
            data=json.dumps(apiPostData),
            request=request,
            post_content_type='json'
            )
        
        if isinstance(apiPost, HttpResponse):
            return apiPost

        return redirect(to=reverse_lazy('frontend:currentHome'))

class CurrentStockUpload(LoginRequiredMixin, View):

    def post(self,request):
        
        reader = csvread(request=request,form_handle='file')
        current_post = []
        for row in reader:
            if row[2] != "":
                current_post.append(
                {
                    "part": row[0],
                    "currentStock": row[2]
                }
                )
        current_post.pop(0)
        # print(json.dumps(current_post))
        
        api = request.build_absolute_uri(reverse_lazy('api:currentstock-list'))
        
        apiPost = api_post(url= api, request=request, data= json.dumps(current_post), post_content_type='json')

        if isinstance(apiPost, HttpResponse):
            return apiPost

        return redirect(to=reverse_lazy('frontend:currentHome'))


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

        if isinstance(dashGet, HttpResponse):
            return dashGet
        if isinstance(typeGet, HttpResponse):
            return typeGet


        data ={'dash':dashGet.json(), 'types':typeGet.json(), 'module':'Minimum Stock'}
        
        return render(request, template_name=self.template_name, context=data)

class MinStockUpdate(LoginRequiredMixin, View):

    def get(self,request):
        return redirect(to=reverse_lazy('frontend:minHome'))

    def post(self,request):
        print(request.POST)

        partUrl = request.build_absolute_uri(reverse_lazy('api:part-list'))
        partGet = api_get(url= partUrl, request= request)
        partData = partGet.json()

        updateQuantity = request.POST.getlist('new_quantity')

        apiPostData = []

        for count,val in enumerate(updateQuantity):
            if val != "":
                apiPostData.append({
                    'part': partData[count]['url'],
                    'minimumStock': int(val)
                })

        print(apiPostData)
        minStockUrl = request.build_absolute_uri(reverse_lazy('api:minstock-list'))

        apiPost =api_post(
            url= minStockUrl,
            data=json.dumps(apiPostData),
            request=request,
            post_content_type='json'
            )
        
        if isinstance(apiPost, HttpResponse):
            return apiPost

        return redirect(to=reverse_lazy('frontend:minHome'))

class MinimumStockUpload(LoginRequiredMixin, View):

    def post(self,request):
        
        reader = csvread(request=request,form_handle='file')
        current_post = []
        for row in reader:
            if row[2] != "":
                current_post.append(
                {
                    "part": row[0],
                    "minimumStock": row[2]
                }
                )
        current_post.pop(0)
        # print(json.dumps(current_post))
        
        api = request.build_absolute_uri(reverse_lazy('api:minstock-list'))
        
        apiPost = api_post(url= api, request=request, data= json.dumps(current_post), post_content_type='json')

        if isinstance(apiPost, HttpResponse):
            return apiPost

        return redirect(to=reverse_lazy('frontend:minHome'))


def logoutRedirect(request):
    # print(request)
    logout(request=request)
    
    return HttpResponseRedirect(redirect_to=reverse('frontend:home'))