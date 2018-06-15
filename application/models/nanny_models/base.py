from django.db import models
import requests
import json
import os
from django.forms import model_to_dict
from uuid import UUID


class ApiCalls(models.Manager):
    nanny_prefix = os.environ.get('APP_NANNY_GATEWAY_URL')

    def __init__(self):
        super(ApiCalls, self).__init__
        self.model_type = self.model

    def get_record(self, **kwargs):
        for field in kwargs:
            query_url = self.nanny_prefix + '/api/v1/' + self.model_type.__name__ + \
                        '/?' + str(field) + '=' + str(kwargs[field])

        if query_url:
            response = requests.get(query_url)

            if response.status_code == 200:
                response.record = json.loads(response.content.decode("utf-8"))[0]
            else:
                response.record = None

            return response

    def create(self, **kwargs):
        model_record = self.model_type()
        model_dict = model_to_dict(model_record)
        request_params = {**model_dict, **kwargs}

        return requests.post(self.nanny_prefix + '/api/v1/' + self.model_type.__name__ + '/', data=request_params)

    def put(self, record, **kwargs):  # Update a record.
        response = requests.put(self.nanny_prefix + '/api/v1/' + self.model_type.__name__ + '/'
                                + record['application_id'] + '/',
                                data=record)
        return response
