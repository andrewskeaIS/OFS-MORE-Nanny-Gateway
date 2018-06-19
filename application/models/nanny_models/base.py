from django.db import models
import requests
import json
import os
from django.forms import model_to_dict


class ApiCalls(models.Manager):
    nanny_prefix = os.environ.get('APP_NANNY_GATEWAY_URL')
    model_name = ""

    def __init__(self, model_name):
        super(ApiCalls, self).__init__()
        self.model_name = model_name

    def get_record(self, **kwargs):
        for field in kwargs:
            query_url = self.nanny_prefix + '/api/v1/' + self.model_name + \
                        '/?' + str(field) + '=' + str(kwargs[field])

        if query_url:
            response = requests.get(query_url)

            if response.status_code == 200:
                response.record = json.loads(response.content.decode("utf-8"))[0]
            else:
                response.record = None

            return response

    def create(self, **kwargs):
        model_type = kwargs.pop("model_type")
        model_record = model_type()
        model_dict = model_to_dict(model_record)
        request_params = {**model_dict, **kwargs}

        return requests.post(self.nanny_prefix + '/api/v1/' + self.model_name + '/', data=request_params)

    def put(self, record, **kwargs):  # Update a record.
        response = requests.put(self.nanny_prefix + '/api/v1/' + self.model_name + '/'
                                + record['childcare_address_id'] + '/',
                                data=record)
        return response
