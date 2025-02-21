from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="users"),
    path("user/", UserDetailView.as_view(), name="user-detail"),
    path("task-form/", TaskFormView.as_view(), name="task-form"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refresh token endpoint
]
