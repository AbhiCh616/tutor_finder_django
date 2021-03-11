from django.urls import path
from accounts.api.views import(
    UserCreate
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create/', UserCreate.as_view(), name='create'),
    path('login/', obtain_auth_token, name='login'),
]