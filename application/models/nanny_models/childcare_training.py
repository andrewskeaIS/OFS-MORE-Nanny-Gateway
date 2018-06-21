from uuid import uuid4

from rest_framework import serializers
from .base import ApiCalls
from django.db import models

from .application import NannyApplication


class ChildcareTraining(models.Model):
    """
    Model for Childcare Training table.
    """
    objects = models.Manager()
    api = ApiCalls("childcare-training")

    childcare_training_id = models.UUIDField(primary_key=True, default=uuid4)
    application_id = models.ForeignKey(NannyApplication, on_delete=models.CASCADE, db_column='application_id')
    level_2_training = models.NullBooleanField(blank=True, null=True, default=None)
    common_core_training = models.NullBooleanField(blank=True, null=True, default=None)
    no_training = models.NullBooleanField(blank=True, null=True, default=None)

    @classmethod
    def get_id(cls, app_id):
        return cls.objects.get(pk=app_id)

    class Meta:
        db_table = 'CHILDCARE_TRAINING'
        # app_label = 'nanny_models'


class ChildcareTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildcareTraining
        fields = '__all__'
