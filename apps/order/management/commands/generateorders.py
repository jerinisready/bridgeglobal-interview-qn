from datetime import datetime

from django.core.management import BaseCommand
import random

from apps.order.models import Order, OrderStatus

ONE_MILLION = 1_000_000
BATCH_SIZE = 250


class Command(BaseCommand):

    def handle(self, **options):
        print("WE ARE GOOD TO GO TO LOAD 1M ORDERS INTO THE SYSTEM")
        print("STARTING ON:", datetime.now().time())
        orders = [Order()] * ONE_MILLION
        Order.objects.bulk_create(orders, ignore_conflicts=True, batch_size=BATCH_SIZE, )

        print("Now Processing with Order Statuses...")
        OrderStatus.objects.all().delete()          # cleaning db; if exists

        for batch_index in range(0, ONE_MILLION, BATCH_SIZE):
            order_status = []
            print("Processing Orders", batch_index, 'to', batch_index + BATCH_SIZE)
            for order in Order.objects.order_by('id')[batch_index: batch_index+BATCH_SIZE]:
                order_status.append(OrderStatus(order=order))
                order_status.append(OrderStatus(order=order, status=random.choice([OrderStatus.CANCELLED, OrderStatus.COMPLETED])))
            OrderStatus.objects.bulk_create(order_status, ignore_conflicts=True, batch_size=BATCH_SIZE)

        print("COMPLETED ON:", datetime.now().time())
        print("THANK YOU! YOU HAVE SUCCESSFULLY COMPLETED LOADING 1M ORDERS INTO THE SYSTEM")

