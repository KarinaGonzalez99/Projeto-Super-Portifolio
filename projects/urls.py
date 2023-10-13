from django.urls import path, include
from .views import (
    ProfileList,
    ProfileDetail,
    ProjectList,
    ProjectDetail,
    ProfileViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'certifying-institutions', CertifyingInstitutionViewSet)
router.register(r'certificates', CertificateViewSet)

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('', include(router.urls)),
]
