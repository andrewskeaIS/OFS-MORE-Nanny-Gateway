from django.db import models
import requests
import json
from django.forms import model_to_dict
from uuid import UUID

class ApiCalls(models.Manager):

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

    def build(self, model_record, **kwargs):
        model_dict = model_to_dict(model_record)
        request_params = {**model_dict, **kwargs}

        return requests.post(self.nanny_prefix + '/api/v1/' + self.model_name + '/', data=request_params)
