from django.contrib.auth import get_user_model
from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import * 
# Create your views here.

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer