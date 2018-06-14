import json
import os
import requests

from uuid import uuid4, UUID

from rest_framework import serializers
from .base import ApiCalls
from django.forms import model_to_dict
from django.db import models
from django.core.validators import RegexValidator


class ApplicationApiCalls(ApiCalls):
    nanny_prefix = os.environ.get('APP_NANNY_GATEWAY_URL')

    # Get a list of records by query.
    def get_record(self,
                   application_id=None,
                   application_type=None,
                   application_status=None,
                   cygnum_urn=None,
                   login_details_status=None,
                   login_details_arc_flagged=None,
                   personal_details_status=None,
                   personal_details_arc_flagged=None,
                   childcare_address_status=None,
                   childcare_address_arc_flagged=None,
                   first_aid_training_status=None,
                   first_aid_training_arc_flagged=None,
                   childcare_training_status=None,
                   childcare_training_arc_flagged=None,
                   criminal_record_check_status=None,
                   criminal_record_check_arc_flagged=None,
                   insurance_cover_status=None,
                   insurance_cover_arc_flagged=None,
                   declarations_status=None,
                   references_status=None,
                   share_info_declare=None,
                   display_contact_details_on_web=None,
                   suitable_declare=None,
                   information_correct_declare=None,
                   change_declare=None,
                   date_created=None,
                   date_updated=None,
                   date_accepted=None,
                   date_submitted=None,
                   application_reference=None,
                   ofsted_visit_email_sent=None):

        fields = locals()
        for field in fields:
            if field:
                query_url = self.nanny_prefix + 'api/v1/application/?' + str(field) + '=' + field

        if query_url:
            response = requests.get(query_url)

            if response.status_code == 200:
                response.record = json.loads(response.content.decode("utf-8"))[0]
            else:
                response.record = None

            return response

    def create(self, **kwargs):  # Create a record.
        model_record = Application()
        model_dict = model_to_dict(model_record)
        request_params = {**model_dict, **kwargs}
        if not isinstance(request_params['application_id'], UUID):
            raise TypeError('The application id must be an instance of uuid')

        response = requests.post(self.nanny_prefix + 'api/v1/application/', data=request_params)

        return response

    def put(self, application_record, **kwargs):  # Update a record.
        response = requests.put(self.nanny_prefix + 'api/v1/application/' + application_record['application_id'] + '/',
                                data=application_record)
        return response


class Application(models.Model):
    """
        Model for Nanny Application table
    """
    # Managers
    objects = models.Manager()
    api = ApiCalls()
    APP_STATUS = (
        ('ARC_REVIEW', 'ARC_REVIEW'),
        ('CANCELLED', 'CANCELLED'),
        ('CYGNUM_REVIEW', 'CYGNUM_REVIEW'),
        ('DRAFTING', 'DRAFTING'),
        ('FURTHER_INFORMATION', 'FURTHER_INFORMATION'),
        ('NOT_REGISTERED', 'NOT_REGISTERED'),
        ('REGISTERED', 'REGISTERED'),
        ('REJECTED', 'REJECTED'),
        ('SUBMITTED', 'SUBMITTED'),
        ('WITHDRAWN', 'WITHDRAWN')
    )
    APP_TYPE = (
        ('CHILDMINDER', 'CHILDMINDER'),
        ('NANNY', 'NANNY'),
        ('NURSERY', 'NURSERY'),
        ('SOCIAL_CARE', 'SOCIAL_CARE')
    )
    TASK_STATUS = (
        ('NOT_STARTED', 'NOT_STARTED'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
        ('FLAGGED', 'FLAGGED')
    )
    application_id = models.UUIDField(primary_key=True, default=uuid4)
    application_type = models.CharField(choices=APP_TYPE, max_length=50, blank=True)
    application_status = models.CharField(choices=APP_STATUS, max_length=50, blank=True)
    cygnum_urn = models.CharField(max_length=50, blank=True)
    login_details_status = models.CharField(choices=TASK_STATUS, max_length=50)
    login_details_arc_flagged = models.BooleanField(default=False)
    personal_details_status = models.CharField(choices=TASK_STATUS, max_length=50)
    personal_details_arc_flagged = models.BooleanField(default=False)
    childcare_address_status = models.CharField(choices=TASK_STATUS, max_length=50)
    childcare_address_arc_flagged = models.BooleanField(default=False)
    first_aid_training_status = models.CharField(choices=TASK_STATUS, max_length=50)
    first_aid_training_arc_flagged = models.BooleanField(default=False)
    childcare_training_status = models.CharField(choices=TASK_STATUS, max_length=50)
    childcare_training_arc_flagged = models.BooleanField(default=False)
    criminal_record_check_status = models.CharField(choices=TASK_STATUS, max_length=50)
    criminal_record_check_arc_flagged = models.BooleanField(default=False)
    insurance_cover_status = models.CharField(choices=TASK_STATUS, max_length=50)
    insurance_cover_arc_flagged = models.BooleanField(default=False)
    declarations_status = models.CharField(choices=TASK_STATUS, max_length=50)
    references_status = models.CharField(choices=TASK_STATUS, max_length=50)
    share_info_declare = models.NullBooleanField(blank=True, null=True, default=None)
    display_contact_details_on_web = models.NullBooleanField(blank=True, null=True, default=None)
    suitable_declare = models.NullBooleanField(blank=True, null=True, default=None)
    information_correct_declare = models.NullBooleanField(blank=True, null=True, default=None)
    change_declare = models.NullBooleanField(blank=True, null=True, default=None)
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    date_accepted = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    application_reference = models.CharField(blank=True, null=True, max_length=9,
                                             validators=[RegexValidator(r'(\w{2})([0-9]{7})')])
    ofsted_visit_email_sent = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_id(cls, app_id):
        return cls.objects.get(pk=app_id)

    class Meta:
        db_table = 'NANNY_APPLICATION'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

