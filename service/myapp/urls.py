from django.urls import path
from .views import QueryDetailView, QueryHistoryView

urlpatterns = [
    path('query/<str:cadastre_number>/', QueryDetailView.as_view(), name='query-detail'),
    path('history/', QueryHistoryView.as_view(), name='query-history'),
]
