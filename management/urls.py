from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Set up the router
router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('library', LibraryHistoryViewSet, basename='library')
router.register('fees', FeesHistoryViewSet, basename='fees')

# Application URL patterns
urlpatterns = [
    # API endpoints
    path('', include((router.urls, 'app_name'))),

    # Authentication routes
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
