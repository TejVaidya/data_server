from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DataViewSet, MyTokenObtainPairView, UserRegistrationView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()
router.register(r'user',UserViewSet,
                basename = 'user')

router.register(r'data',DataViewSet,
                basename = 'data')

urlpatterns += router.urls