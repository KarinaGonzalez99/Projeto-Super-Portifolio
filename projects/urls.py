from django.urls import path, include
from .views import (
    ProfileList,
    ProfileDetail,
    ProjectList,
    ProjectDetail,
    ProfileViewSet,
    )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('projects/', ProjectList.as_view(), name='project-list', ProfileViewSet),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail', ProfileViewSet),
    path('', include(router.urls)),
]
