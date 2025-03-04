from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from blog.serializers import UserCreationSerializer,PostSerializer,CommentSerializer

from blog.models import Post

from rest_framework import authentication,permissions


class CreateUserView(CreateAPIView):

    serializer_class=UserCreationSerializer

class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
class PostReterieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

class CommentCreateView(CreateAPIView):

    serializer_class=CommentSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        id=self.kwargs.get("pk")

        post_instance=get_object_or_404(Post,id=id)

        serializer.save(post_object=post_instance,owner=self.request.user)
    

