import random
import time

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .models import Query, ExternalServerResponse
from .serializers import QuerySerializer, ExternalServerSerializer


class QueryDetailView(CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def perform_create(self, serializer):
        query_instance = serializer.save()
        sleep_time = random.randint(5, 60)
        time.sleep(sleep_time)
        ExternalServerResponse.objects.create(query=query_instance, result=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QueryHistoryView(ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class ServerResponceView(CreateAPIView):
    queryset = ExternalServerResponse.objects.all()
    serializer_class = ExternalServerSerializer
