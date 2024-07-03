import random
import requests
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse
from django.conf import settings
from .models import Query
from .serializers import QuerySerializer


class QueryDetailView(CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        query_instance = serializer.instance
        response = requests.post(f"{settings.INTERNAL_HOST}{reverse('server-response')}",
                                 json={"query_id": query_instance.id})
        if response.status_code == 200:
            result = response.json().get("result")
            return Response({"result": result}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"error": "Failed to get response from external server"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=headers)


class QueryHistoryView(ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class QueryDetailByNumberView(ListAPIView):
    serializer_class = QuerySerializer

    def get_queryset(self):
        number = self.kwargs['number']
        return Query.objects.filter(number=number)


class ServerResponseView(APIView):
    def post(self, request, *args, **kwargs):
        query_id = request.data.get('query_id')
        if not query_id:
            return Response({'error': 'query_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            query = Query.objects.get(id=query_id)
        except Query.DoesNotExist:
            return Response({'error': 'Query not found'}, status=status.HTTP_404_NOT_FOUND)

        result = random.choice([True, False])

        return Response({'query_id': query_id, 'result': result}, status=status.HTTP_200_OK)
