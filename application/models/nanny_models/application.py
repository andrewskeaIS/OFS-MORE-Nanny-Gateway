import json
import os
import requests

from uuid import uuid4, UUID

from rest_framework import serializers
from django.db import models
from django.forms import model_to_dict


class ApiCalls(models.Manager):

    identity_prefix = os.environ.get('APP_IDENTITY_URL')

    # def get_record(self, email=None, pk=None, magic_link_email=None, magic_link_sms=None):  # Get a list of records by query.
    #     if email is not None:
    #         query_url = self.identity_prefix + 'api/v1/user/?email=' + email
    #     elif pk is not None:
    #         query_url = self.identity_prefix + 'api/v1/user?login_id=' + pk
    #     elif magic_link_email is not None:
    #         query_url = self.identity_prefix + 'api/v1/user?magic_link_email=' + magic_link_email
    #     elif magic_link_sms is not None:
    #         query_url = self.identity_prefix + 'api/v1/user?magic_link_sms=' + magic_link_sms
    #
    #     response = requests.get(query_url)
    #
    #     if response.status_code == 200:
    #         response.record = json.loads(response.content.decode("utf-8"))[0]
    #     else:
    #         response.record = None
    #
    #     return response
    #
    # def create(self, **kwargs):  # Create a record.
    #     model_record = UserDetails()
    #     model_dict = model_to_dict(model_record)
    #     request_params = {**model_dict, **kwargs}
    #     if not isinstance(request_params['application_id'], UUID):
    #         raise TypeError('The application id must be an instance of uuid')
    #
    #     response = requests.post(self.identity_prefix + 'api/v1/user/', data=request_params)
    #
    #     return response
    #
    # def put(self, user_details_record, **kwargs):  # Update a record.
    #     response = requests.put(self.identity_prefix + 'api/v1/user/' + user_details_record['login_id'] + '/', data=user_details_record)
    #     return response


class Application(models.Model):
    """
    Test
    """
    # Managers
    objects = models.Manager()
    api = ApiCalls()

    @property
    def timelog_fields(self):
        """
        Specify which fields to track in this model once application is returned.

        Used for signals only. Check base.py for available signals.
        This is used for logging fields which gonna be updated by applicant
        once application status changed to "FURTHER_INFORMATION" on the arc side

        Returns:
            tuple of fields which needs update tracking when application is returned
        """

        return (
        )

    class Meta:
        db_table = 'APPLICATION'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        # fields = ('login_id', 'email', 'mobile_number', 'add_phone_number', 'email_expiry_date', 'sms_expiry_date',
        #           'magic_link_email', 'magic_link_sms', 'sms_resend_attempts', 'sms_resend_attempts_expiry_date', 'application_id')