from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from destinationguidesapi.models import Country, Region

class CountryView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      country = Country.objects.get(pk=pk)
      
      serializer = CountrySerializer(country)
      return Response(serializer.data)
    except Country.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def list(self, request):
    
    countrys = Country.objects.all()
    
    serializer = CountrySerializer(countrys, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    region = Region.objects.get(pk=request.data["region"])
    
    country = Country.objects.create(
      name = request.data["name"],
      region=region
    )
    
    serializer = CountrySerializer(country)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    
    region = Region.objects.get(pk=request.data["region"])
    
    id = pk
    country = Country.objects.get(pk=pk)
    
    country.name = request.data["name"]
    country.region = region
    
    country.save()
    
    serializer = CountrySerializer(country)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    
    country = Country.objects.get(pk=pk)
    
    country.delete()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  
class CountrySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Country
    fields = ('id', 'name', 'region')
    