from django.urls import path, include
from rest_framework import routers
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet
)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"profiles/<int: id>", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"projects/<int:id>", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
