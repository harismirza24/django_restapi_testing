from rest_framework import serializers
from firstapp.models import CarSpecs

class SerializeCarSpecs(serializers.ModelSerializer):
    extra_field = serializers.SerializerMethodField("get_extra")
    


    def get_extra(self,car_object):
        return 21
    
    class Meta:
        model = CarSpecs
        fields = "__all__"
      