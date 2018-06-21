from uuid import uuid4

from rest_framework import serializers
from .base import ApiCalls
from django.db import models
from .nanny_application import NannyApplication


class ApplicantPersonalDetails(models.Model):
    """
        Model for Nanny Application table
    """
    # Managers
    objects = models.Manager()
    api = ApiCalls("applicant-personal-details", "personal_detail_id")

    application_id = models.ForeignKey(NannyApplication, on_delete=models.CASCADE, db_column='application_id')
    personal_detail_id = models.UUIDField(primary_key=True, default=uuid4)
    birth_day = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)

    @classmethod
    def get_id(cls, personal_detail_id):
        return cls.objects.get(pk=personal_detail_id)

    class Meta:
        db_table = 'APPLICANT_PERSONAL_DETAILS'


class ApplicantPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantPersonalDetails
        fields = '__all__'
