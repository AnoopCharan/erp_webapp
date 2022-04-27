from traceback import print_tb
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api import models, serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
import json

# Create your views here.

class UnitMeasureMVS(ModelViewSet):
    queryset = models.UnitMeasure.objects.all()
    serializer_class = serializers.UnitMeasureSerializer
    filter_fields = {
        'unit':['icontains', 'iregex', 'exact']
    }
    

class StatusMVS(ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    filter_fields = {
        'status':['icontains', 'iregex', 'exact']
    }

class PeopleMVS(ModelViewSet):
    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer
    filter_fields = {
        'firstName':['icontains', 'iregex', 'exact'],
        'lastName':['icontains', 'iregex', 'exact'],
        'email':['icontains', 'iregex', 'exact'],
    }

class AttachmentMVS(ModelViewSet):
    queryset = models.Attachment.objects.all()
    serializer_class = serializers.AttachmentSerializer
    filter_fields = {
        'fileName':['icontains', 'iregex', 'exact'],
        'contentType':['icontains', 'iregex', 'exact'],
    }

    def create(self, request, *args, **kwargs):
        print(request.data)
        # print(">>>>>>>>>>>",request.data['attachedFile'].content_type)
        # print(">>>>>>>>>>>",request.data['attachedFile'].name)

        # print(">>>>>>>>>>>",dir(request.data['attachedFile']))
        data = request.data
        
        data['contentType']= request.data['attachedFile'].content_type
        data['fileName']= request.data['attachedFile'].name
            
        print(data)
        postSerializer = self.serializer_class(data= data, context={'request': request})

        if postSerializer.is_valid():
            postSerializer.save()
            return Response(data=postSerializer.data, status=HTTP_201_CREATED)
        else:
            return Response(data=postSerializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)

class PartCategoryMVS(ModelViewSet):
    queryset = models.PartCategory.objects.all()
    serializer_class = serializers.PartCategorySerializer
    filter_fields = {
        'category':['exact','icontains','iregex']
    }

class SupplierMVS(ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    filter_fields = {
        'name':['exact','icontains','iregex'],
        'poc__firstName':['exact','icontains','iregex'],
        'poc__lastName':['exact','icontains','iregex'],
        'address':['exact','icontains','iregex'],
    }

class PartMVS(ModelViewSet):
    queryset = models.Part.objects.all()
    serializer_class = serializers.PartSerializer
    filter_fields = {
        'name':['exact','icontains','iregex'],
        'category__category':['exact','icontains','iregex'],
        'supplier__name':['exact','icontains','iregex'],
    }


class MinimumStockMVS(ModelViewSet):
    queryset = models.MinimumStock.objects.all()
    serializer_class = serializers.MinimumStockSerializer
    filter_fields = {
        'part':['exact'],
        'part__name':['icontains', 'iregex', 'exact'],
        'part__category__category':['icontains', 'iregex', 'exact'],
        'minimumStock': ['exact','gt','lt','gte','lte'],
        'lastUpdateDate': ['exact','gt','lt','gte','lte']
    }

class CurrentStockMVS(ModelViewSet):
    queryset = models.CurrentStock.objects.all()
    serializer_class = serializers.CurrentStockSerializer
    filter_fields = {
        'part':['exact'],
        'part__name':['icontains', 'iregex', 'exact'],
        'part__category__category':['icontains', 'iregex', 'exact'],
        'currentStock': ['exact','gt','lt','gte','lte'],
        'lastUpdateDate': ['exact','gt','lt','gte','lte']
    }

class OrderMVS(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_fields = {
        'part':['exact'],
        'poNumber': ['exact','gt','lt','gte','lte'],
        'part__name':['icontains', 'iregex', 'exact'],
        'part__category__category':['icontains', 'iregex', 'exact'],
        'quantity': ['exact','gt','lt','gte','lte'],
        'dateOrdered': ['exact','gt','lt','gte','lte'],
        'eta': ['exact','gt','lt','gte','lte'],
        'dateDelivered': ['exact','gt','lt','gte','lte'],
        'status': ['exact'],
        'unit__unit':['icontains', 'iregex', 'exact'],
    }


class ReceivingMVS(ModelViewSet):
    queryset = models.Receiving.objects.all()
    serializer_class = serializers.ReceivingSerializer
    filter_fields = {
        'orderItem':['exact'],
        'orderItem__poNumber':['icontains', 'iregex', 'exact'],
        'orderItem__part__name':['icontains', 'iregex', 'exact'],
        'quantity': ['exact','gt','lt','gte','lte'],
        'date': ['exact','gt','lt','gte','lte']
    }

class Dash(ModelViewSet):
    # modified method to get custom queryset for dashboard table in landing page
    # added filtering fuctionality using basic url parameters and ORM filtering
    serializer_class= serializers.MinimumStockSerializer 
    
    def get_queryset(self):
        sql="""
                SELECT * 
                FROM
                (SELECT *, pid_1 AS id
                FROM 
                (SELECT pid_1,minimumStock AS min_stock, currentStock AS current_stock, led AS expected_by, totord AS on_order, crecent AS recent_update  
                FROM
                    (SELECT * 
                        FROM
                        (SELECT * 
                        FROM
                        (SELECT part_id AS pid_1, max(lastUpdateDate) AS crecent
                        FROM api_MinimumStock
                        group by part_id) AS t 
                    JOIN api_MinimumStock AS m ON m.part_id = t.pid_1 and t.crecent = m.lastUpdateDate ) AS t1,
                        (SELECT * 
                        FROM
                        (SELECT part_id AS pid_2, max(lastUpdateDate) AS recent
                        FROM stock_stock_current
                        group by part_id) AS ta 
                    JOIN stock_stock_current AS mi ON mi.part_id = ta.pid_2 and ta.recent = mi.lastUpdateDate ) AS t2
                    WHERE t1.pid_1= t2.pid_2) AS b1
                left JOIN 
                    (SELECT part_id AS pid_3, max(expected_by_date) AS led, sum(quantity_ordered) AS totord
                    FROM orders_orders_table
                    group by part_id) AS b2 
                ON b1.pid_1 = b2.pid_3) out1

                JOIN 

                (SELECT p.id AS pid_0 , part_name, part_type FROM stock_stock_parts AS p
                JOIN stock_part_category AS c 
                ON p.part_type_id = c.id
                ) AS out2

                ON out2.pid_0 = out1.pid_1

                ORDER BY id ASC) AS  ft
                """
        
        queryset= models.Part.objects.raw(sql)
       

        return queryset
