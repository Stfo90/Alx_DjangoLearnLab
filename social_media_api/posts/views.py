from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        # Get the users that the current user follows
        following_users = request.user.following.all()
        
        # Get the posts from users the current user follows, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        
        # Return the serialized posts as a response
        return Response(serializer.data)




class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(user=request.user, post=post)
        
        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked",
            target=post
        )
        
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
