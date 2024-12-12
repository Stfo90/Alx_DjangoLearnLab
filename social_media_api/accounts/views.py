from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response(
                    {"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST
                )
            request.user.following.add(user_to_follow)
            return Response(
                {"message": f"You are now following {user_to_follow.username}."},
                status=status.HTTP_200_OK,
            )
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            if user_to_unfollow == request.user:
                return Response(
                    {"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST
                )
            request.user.following.remove(user_to_unfollow)
            return Response(
                {"message": f"You have unfollowed {user_to_unfollow.username}."},
                status=status.HTTP_200_OK,
            )
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UserListView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
