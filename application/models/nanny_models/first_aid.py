from uuid import uuid4
from django.db import models
from rest_framework import serializers

from .base import ApiCalls
from .nanny_application import NannyApplication


class FirstAidTraining(models.Model):
    """
    Model for FIRST_AID_TRAINING table
    """
    objects = models.Manager()
    api = ApiCalls("first_aid_training", 'first_aid_id')
    first_aid_id = models.UUIDField(primary_key=True, default=uuid4)
    application_id = models.ForeignKey(
        NannyApplication, on_delete=models.CASCADE, db_column='application_id')
    training_organisation = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_date = models.DateField()
    show_certificate = models.NullBooleanField(blank=True, null=True, default=None)
    renew_certificate = models.NullBooleanField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'FIRST_AID_TRAINING'


class FirstAidTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAidTraining
        fields = '__all__'

