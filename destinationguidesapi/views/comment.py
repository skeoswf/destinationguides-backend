"""View module for handling requests about comments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from destinationguidesapi.models import Comment, User, Post


class CommentView(ViewSet):

    def retrieve(self, request, pk):

        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
    
        comments = Comment.objects.all()
        
        post = request.query_params.get('post', None)
        
        if post is not None:
            comments = comments.filter(post=post)
        
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
      
    def create(self, request):

      commenter = User.objects.get(uid=request.data["commenter"])
      post = Post.objects.get(pk=request.data["post"])

      comment = Comment.objects.create(
          commenter=commenter,
          post=post,
          text=request.data["text"],
      )
      serializer = CommentSerializer(comment)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  
    def update(self, request, pk):
      
        commenter = User.objects.get(uid=request.data["commenter"])
        post = Post.objects.get(pk=request.data["post"])
    
        comment = Comment.objects.get(pk=pk)
        comment.commenter=commenter
        comment.post=post
        comment.text=request.data["text"]
        comment.save()
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
  
       
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comment
        fields = ('id', 'commenter', 'post', 'text')
