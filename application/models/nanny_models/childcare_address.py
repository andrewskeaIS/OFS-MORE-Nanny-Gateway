from uuid import uuid4

from rest_framework import serializers
from .base import ApiCalls
from django.db import models
from .nanny_application import NannyApplication


class ChildcareAddress(models.Model):
    """
        Model for Nanny Application table
    """
    # Managers
    objects = models.Manager()
    api = ApiCalls("childcare-address")

    application_id = models.ForeignKey(NannyApplication, on_delete=models.CASCADE, db_column='application_id')
    childcare_address_id = models.UUIDField(primary_key=True, default=uuid4)
    street_line1 = models.CharField(max_length=100)
    street_line2 = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    address_to_be_provided = models.NullBooleanField(blank=True, null=True, default=None)

    @classmethod
    def get_id(cls, childcare_address_id):
        return cls.objects.get(pk=childcare_address_id)

    class Meta:
        db_table = 'CHILDCARE_ADDRESS'


class ChildcareAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildcareAddress
        fields = '__all__'
