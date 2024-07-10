from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Data, User
from .serializers import DataSerializer, UserSerializer, RegisterUserSerializer, MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    
    def list(self, request, *args, **kwargs):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
     
    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    @action(default=False, methods = ['post'])
    def write_data(self, request, *args, **kwargs):
        data = request.data
        Data.objects.create(value = data.get("value"),
                            description = data.get("description"),
                            cost = data.get("cost"),
                            business_unit = data.get("business_unit"),
                            valid_data = False)
        
    @action(default=False, methods = ['post'])
    def approve_data(self, request, *args, **kwargs):
        data = Data.objects.get(id = int(request.data.get('data_id')))
        if data:
            if request.user["role"].lower() == 'admin':
                data.valid_data = True
                data.save()
                            
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if User.objects.filter(username=request.data['username']).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = (AllowAny,)
    
