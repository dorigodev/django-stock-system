from django.urls import path
from django.urls import include
from apps.users.views import create_User, login_User, logout_User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', create_User, name="create_user"),
    path('login', login_User, name="login_user"),
    path('logout', logout_User, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

