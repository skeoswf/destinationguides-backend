from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from destinationguidesapi.models import Post, User, Category, Country, Region, Tag

class PostView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try: 
      post = Post.objects.get(pk=pk)
      
      serializer = PostSerializer(post)
      return Response(serializer.data)
    
    except Post.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    
    ## GET THE CATEGORY FROM THE REQUEST PARAMS
    category = request.query_params.get('category', None)
    ## GET THE AUTHOR FROM THE REQUEST PARAMS
    author = request.query_params.get('author', None)
    ## GET THE COUNTRY FROM THE REQUEST PARAMS
    country = request.query_params.get('country', None)
    ## GET THE REGION FROM THE REQUEST PARAMS
    region = request.query_params.get('region', None)
    
    posts = Post.objects.all()
    
    if category is not None:
      posts = posts.filter(category=category)
      
    if author is not None:
      posts = posts.filter(author=author)
      
    if country is not None:
      posts = posts.filter(country=country)
      
    if region is not None:
      posts = posts.filter(region=region)
    
    # GET THE TAGS FOR THE POSTS
    for post in posts:
      tags = Tag.objects.filter(posttag__post_id=post)
      post.tags=tags.all()
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    ## may need to update pk to uid depending on what FE does
    author = User.objects.get(pk=request.data["author"])
    category = Category.objects.get(pk=request.data["category"])
    country = Country.objects.get(pk=request.data["country"])
    region = Region.objects.get(pk=request.data["region"])
    
    post = Post.objects.create(
      title=request.data["title"],
      author=author,
      category=category,
      body=request.data["body"],
      country=country,
      region=region,
      image=request.data["image"]
      ## created_at will automatically be set to current date and time?
    )
    
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    
    author = User.objects.get(pk=request.data["author"])
    category = Category.objects.get(pk=request.data["category"])
    country = Country.objects.get(pk=request.data["country"])
    region = Region.objects.get(pk=request.data["region"])
    
    id = pk
    post = Post.objects.get(pk=pk)
    
    post.title=request.data["title"]
    post.author=author
    post.category=category
    post.body=request.data["body"]
    post.country=country
    post.region=region
    post.image=request.data["image"]
    
    post.save()
    
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    
    post = Post.objects.get(pk=pk)
    
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class TagSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tag
    fields = ('id', 'name')
    
class PostSerializer(serializers.ModelSerializer):
  
  tags = TagSerializer(read_only=True, many=True)
  class Meta:
    model = Post
    fields = ('id', 'title', 'author', 'category', 'body', 'country', 'region', 'image', 'created_at', 'tags')
    depth = 1
