from django.urls import path

from apps.order.apis.views import AsyncCancelledOrdersAPIView


urlpatterns = [
    path('cancelled/', AsyncCancelledOrdersAPIView.as_view(), name='cancelled-orders')
]
