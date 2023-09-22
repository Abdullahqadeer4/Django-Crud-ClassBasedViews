from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from crud.models import items,location
from crud.serializers import locationserializer,itemserializer
# def home(request):
#     return render(request,"app/index.html")


# #Write all logical code here



class itemlist(generics.ListCreateAPIView):
    serializer_class=itemserializer
     
    def get_queryset(self):
        queryset=items.objects.all()
        location=self.request.query_params.get('location')
        if location is not None:
            queryset=queryset.filter(itemlocation=location)
        return queryset
        


class locationlist(generics.ListCreateAPIView):
    serializer_class=locationserializer
    queryset=location.objects.all()


class locationdetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=locationserializer
    queryset=location.objects.all()
    
    
class itemdetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=itemserializer
    queryset=items.objects.all()