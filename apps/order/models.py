from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    pass


class OrderStatus(models.Model):
    COMPLETED, PENDING, CANCELLED = range(1, 4)
    COMPLETED_TEXT, PENDING_TEXT, CANCELLED_TEXT = ('Completed', 'Pending', 'Cancelled')

    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=[         #better to use integer than string for filtering and comparision.
        (COMPLETED, COMPLETED_TEXT),
        (PENDING, PENDING_TEXT),
        (CANCELLED, CANCELLED_TEXT),
    ], default=2)               # sot that <2 will be completed and failed, >2 will be pending and cancelled, and != 2 will be final order.
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def status_text(self):
        return (OrderStatus.COMPLETED_TEXT, OrderStatus.PENDING_TEXT, OrderStatus.CANCELLED_TEXT)[self.status+1]

    class Meta:
        indexes = (
            models.Index(fields=['status']),
        )

    def __str__(self):
        return f'{self.order_id} - {self.status_text}'


@receiver(post_save, sender=Order)
def generate_pending_status(sender, instance, created, **kwargs):
    """
    Adding Initial status as pending on creating an order.
    """
    if created:
        OrderStatus.objects.create(order=instance)


