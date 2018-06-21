from uuid import uuid4

from rest_framework import serializers
from .base import ApiCalls
from django.db import models
from .nanny_application import NannyApplication
from .applicant_personal_details import ApplicantPersonalDetails


class ApplicantHomeAddress(models.Model):
    """
        Model for Nanny Application table
    """
    # Managers
    objects = models.Manager()
    api = ApiCalls("applicant-home-address", "home_address_id")

    application_id = models.ForeignKey(NannyApplication, on_delete=models.CASCADE, db_column='application_id')
    personal_detail_id = models.ForeignKey(ApplicantPersonalDetails, on_delete=models.CASCADE,
                                           db_column='personal_detail_id')
    home_address_id = models.UUIDField(primary_key=True, default=uuid4)
    street_line1 = models.CharField(max_length=100, blank=True, null=True)
    street_line2 = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    current_address = models.NullBooleanField(blank=True, null=True, default=None)
    childcare_address = models.NullBooleanField(blank=True, null=True, default=None)
    move_in_month = models.IntegerField(blank=True, null=True)
    move_in_year = models.IntegerField(blank=True, null=True)

    @classmethod
    def get_id(cls, home_address_id):
        return cls.objects.get(pk=home_address_id)

    class Meta:
        db_table = 'APPLICANT_HOME_ADDRESS'


class ApplicantHomeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantHomeAddress
        fields = '__all__'
