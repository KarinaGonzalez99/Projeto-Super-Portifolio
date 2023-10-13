from rest_framework import viewsets
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import (
    ProfileSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
    )
from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated,
)
from .serializers import ProjectSerializer
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method == "GET":
            kwargs.get("pk")
            profile = self.get_object()
            return render(request, "profile_detail.html", {"profile": profile})
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    permission_classes = [IsAuthenticated]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]
