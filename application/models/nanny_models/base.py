from django.db import models
import requests
import json
import os
from django.forms import model_to_dict


class ApiCalls(models.Manager):
    nanny_prefix = os.environ.get('APP_NANNY_GATEWAY_URL')
    model_name = ""
    pk = ""

    def __init__(self, model_name, pk):
        super(ApiCalls, self).__init__()
        self.model_name = model_name
        self.pk = pk

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


    def get_records(self, **kwargs):
        for field in kwargs:
            query_url = self.nanny_prefix + '/api/v1/' + self.model_name + \
                        '/?' + str(field) + '=' + str(kwargs[field])

        if query_url:
            response = requests.get(query_url)

            if response.status_code == 200:
                response.record = json.loads(response.content.decode("utf-8"))
            else:
                response.record = None

            return response

    def create(self, **kwargs):
        model_type = kwargs.pop("model_type")
        model_record = model_type()
        model_dict = model_to_dict(model_record)
        request_params = {**model_dict, **kwargs}

        response = requests.post(self.nanny_prefix + '/api/v1/' + self.model_name + '/', data=request_params)

        if response.status_code == 201:
            response.record = json.loads(response.content.decode("utf-8"))
        else:
            response.record = None

        return response

    def put(self, record, **kwargs):  # Update a record.
        pk_name = self.model._meta.pk.name
        response = requests.put(self.nanny_prefix + '/api/v1/' + self.model_name + '/'
                                + record[pk_name] + '/',
                                data=record)
        return response
