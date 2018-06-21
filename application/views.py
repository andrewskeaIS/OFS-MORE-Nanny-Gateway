from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from application.models.nanny_models.application import NannyApplication, NannyApplicationSerializer
from application.models.nanny_models.childcare_training import ChildcareTraining, ChildcareTrainingSerializer


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        if not queryset.exists():
            raise NotFound(detail="Error 404, resource not found", code=404)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NannyApplicationViewSet(BaseViewSet):
    """
    list:
    List all current applications stored in the database
    create:
    Create a new full application in the database
    retrieve:
    List the application with the corresponding primary key (application_id) from the database
    update:
    Update all fields in a record with the corresponding primary key (application_id) from the database
    partial_update:
    Update any amount of fields in  a record with the corresponding primary key (application_id) from the database
    destroy:
    Delete the application with the corresponding primary key (application_id) from the database
    """
    queryset = NannyApplication.objects.all()
    serializer_class = NannyApplicationSerializer
    filter_fields = (
        'application_id',
    )


class ChildcareTrainingViewSet(BaseViewSet):
    queryset = ChildcareTraining.objects.all()
    serializer_class = ChildcareTrainingSerializer
    filter_fields = (
        'application_id',
    )
