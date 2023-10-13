from django.urls import path, include
from .views import (
    ProfileDetail,
    ProjectList,
    ProjectDetail,
    ProfileViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet
)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'certifying-institutions', CertifyingInstitutionViewSet)
router.register(r'certificates', CertificateViewSet)


urlpatterns = [
    path('profiles/', ProfileViewSet.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
