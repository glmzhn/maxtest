from django.urls import path
from .views import QueryDetailView, QueryHistoryView, ServerResponceView

urlpatterns = [
    path('api/v1/query/', QueryDetailView.as_view(), name='query'),
    path('api/v1/history/', QueryHistoryView.as_view(), name='query-history'),
    path('api/v1/result/', ServerResponceView.as_view(), name='server-responce')
]
