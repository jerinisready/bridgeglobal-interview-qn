from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Max, F
from django.views import View
from asgiref.sync import sync_to_async

from apps.order.models import Order, OrderStatus


class AsyncCancelledOrdersAPIView(View):

    async def get(self, request, *args, **kwargs):
        page_number = request.GET.get('page', 1)
        items_per_page = 10
        cancelled_orders = await sync_to_async(self.get_cancelled_orders)()
        paginator = Paginator(cancelled_orders, items_per_page)

        try:
            cancelled_orders_page = await sync_to_async(paginator.page)(page_number)
        except EmptyPage:
            cancelled_orders_page = await sync_to_async(paginator.page)(paginator.num_pages)
        except Exception as e:
            cancelled_orders_page = await sync_to_async(paginator.page)(1)

        serialized_orders = await sync_to_async(self.serialize_orders)(cancelled_orders_page)
        response_data = {
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': cancelled_orders_page.number,
            'result': serialized_orders,
        }
        return JsonResponse(response_data)

    def get_cancelled_orders(self):
        return (Order.objects.filter(orderstatus__status=OrderStatus.CANCELLED)
                .annotate(latest_status_date=Max('orderstatus__created_at'))
                .filter(orderstatus__created_at=F('latest_status_date'))
                .order_by('-latest_status_date')).values('id', 'latest_status_date')

    @staticmethod
    def serialize_orders(orders):
        return [*orders]
