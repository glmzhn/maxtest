from django.urls import path
from .views import QueryDetailView, QueryHistoryView, ServerResponseView, QueryDetailByNumberView

urlpatterns = [
    path('api/v1/query/', QueryDetailView.as_view(), name='query'),
    path('api/v1/history/', QueryHistoryView.as_view(), name='query-history'),
    path('api/v1/result/', ServerResponseView.as_view(), name='server-response'),
    path('api/v1/history/<str:number>/', QueryDetailByNumberView.as_view(), name='query-detail')
]
