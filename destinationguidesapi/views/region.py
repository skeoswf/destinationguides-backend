from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from destinationguidesapi.models import Region

class RegionView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      region = Region.objects.get(pk=pk)
      
      serializer = RegionSerializer(region)
      return Response(serializer.data)
    except Region.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def list(self, request):
    
    regions = Region.objects.all()
    
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    region = Region.objects.create(
      name = request.data["name"]
    )
    
    serializer = RegionSerializer(region)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    
    id = pk
    region = Region.objects.get(pk=pk)
    
    region.name = request.data["name"]
    
    region.save()
    
    serializer = RegionSerializer(region)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    
    region  = region.objects.get(pk=pk)
    
    region.delete()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  
class RegionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Region
    fields = ('id', 'name')
    