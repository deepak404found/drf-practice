from django.contrib.auth import authenticate
from django.contrib.auth.models import User, update_last_login
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Task
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    TaskSerializer,
    UserSerializer,
)


# ✅ Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# ✅ Login View (using APIView since we need custom logic)
class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                update_last_login(None, user)
                token = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(token),
                        "access": str(token.access_token),
                        "user": UserSerializer(user).data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Get all users (ListAPIView)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# ✅ Get, Update, Delete a user (RetrieveUpdateDestroyAPIView)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Get logged-in user


# ✅ Task Form (CreateAPIView for creating new tasks)
class TaskFormView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
