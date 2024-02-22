from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

class PostListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Post with given post data
        '''
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'username': request.data.get('username')
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,*args,**kwargs):
        '''
        Update the post with the id from the url

        '''
        post_id = kwargs.get('pk')
        if not post_id:
            return Response({"error":"Must provide Post Id"},status = status.HTTP_400_BAD_REQUEST)
        
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error":f"Post with id ({post_id}) does not exist"},status = status.HTTP_404_NOT_FOUND)


        # create empty object to receive allowed fields (if they exist)
        allowed_fields = ['title','content']
        data = {}

        data = {field: request.data[field] for field in allowed_fields if field in request.data}
        #check if any allowed fields exist
        if not data:
            return Response({"error": f"no title or content where sent to update post ({post_id})"}, status=status.HTTP_400_BAD_REQUEST)
        #create serializer for editing the post
        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        '''
        Delete the post with the id from the url
        '''
        post_id = kwargs.get('pk')
        if not post_id:
            return Response({"error": "Must provide Post Id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": f"Post with id ({post_id}) does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        post.delete()
        return Response({}, status=status.HTTP_200_OK)



