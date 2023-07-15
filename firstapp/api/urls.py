from django.urls import path,include
from .views import List_func,Destroy_obj,Put_method
#from .views import First_funct,Destroyset
#from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
#router.register(r'testroute1',First_funct,basename= 'testroute1')
#router.register(r'delete',Destroyset,basename='delete')

urlpatterns = [
    path('first/add/<str:carbody>/',List_func),
    path('first/delete/<int:id>/',Destroy_obj),
    path('first/update/<str:car_brand>/',Put_method),

    #path('first/<str:carbody>',First_funct.as_view({'get':'list'})),# you can do this oryou can use router for urls 
    #path(r'first/<str:carbody>/',include(router.urls)),
    #path(r'first/<int:id>/',include(router.urls)),

]