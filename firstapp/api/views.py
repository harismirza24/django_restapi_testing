from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

#from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from firstapp.api.serializers import SerializeCarSpecs
from firstapp.models import CarSpecs
import random
#user defines functions:
@api_view()
#@permission_classes([AllowAny])
def List_func(request,carbody):
    carspecs = CarSpecs.objects.filter(car_body=carbody)
    if carspecs.exists():
        serializer = SerializeCarSpecs(carspecs,many =True)
        return Response({'data': serializer.data})
    else:
        cars_brands_name = ["Porche","Honda",'Toyota',"Nissan","Buggati"]
        cars = random.choice(cars_brands_name)
        new_car_obj = CarSpecs.objects.create(car_body = carbody,car_brand = cars,car_model = "Lamborghini Aventador",production_year = "2010",engine_type = "one engine",)
        serializer = SerializeCarSpecs(new_car_obj)
        return Response({'data': serializer.data})
@api_view()
def Destroy_obj(request,id):
        queryset = CarSpecs.objects.all()
        alldata = CarSpecs.objects.filter(id=id)
        alldata =alldata.delete()
        serializer = SerializeCarSpecs(queryset,many=True)
        return Response({"data": serializer.data})
@api_view()
def Put_method(request,car_brand):
     data=request.data
     test = CarSpecs.objects.get(car_brand = car_brand)
     test.car_model="Le Ferrari G3"
     test.save()
     print(test) 
     serializer = SerializeCarSpecs(test)
     
     return Response({'data':serializer.data})
    
#class based views:        
"""class First_funct(viewsets.ViewSet):
    #permission_classes = [AllowAny]
    #authentication_classes = [authentication.JWTAuthentication]
    
    

    def list(self,request,carbody):
        
        carspecs = CarSpecs.objects.filter(car_body=carbody)
        alldata = CarSpecs.objects.all()
       
        # for display data in descending according to car_body attribute:
        alldata = alldata.order_by('-car_body')

    
        if carspecs.exists():
            serializer = SerializeCarSpecs(alldata,many =True)

            return Response({'data': serializer.data})
        else:
            cars_brands_name = ["Porche","Honda",'Toyota',"Nissan","Buggati"]
            cars = random.choice(cars_brands_name)
            new_car_obj = CarSpecs.objects.create(car_body = carbody,car_brand = cars,car_model = "Lamborghini Aventador",production_year = "2010",engine_type = "one engine",)
            new_car_obj.save()
            serializer = SerializeCarSpecs(alldata)
            return Response({'data': serializer.data})
class Destroyset(viewsets.ViewSet):

    def list(self,request,id):
        queryset = CarSpecs.objects.all()
        alldata = CarSpecs.objects.filter(id=id)
        alldata =alldata.delete()
        serializer = SerializeCarSpecs(queryset,many=True)
        return Response({"data": serializer.data})
        """
