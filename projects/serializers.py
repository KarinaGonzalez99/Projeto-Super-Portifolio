from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class NestedCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "timestamp"
            ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'id',
            'name',
            'certifying_institution',
            'timestamp',
            'profiles'
            )


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificatesSerializer(many=True, required=False)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificates', [])
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
            )

        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=certifying_institution,
                **certificate_data
            )

        return certifying_institution