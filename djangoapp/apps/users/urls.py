from django.urls import path
from django.urls import include
from apps.users.views import create_User, login_User, logout_User

urlpatterns = [
    path('register_store', create_User, name="create_user"),
    path('login_user', login_User, name="login_user"),
    path('logout', logout_User, name='logout'),
]

