from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    """
    Model class which mapped with the orders table in the database
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def top_5_customers(cls):
        '''
        method to return top most 5 customers in last 6 months
        :return: List of the top most 5 customers in last 6 months
        '''
        six_months_ago = timezone.now() - timedelta(days=6*30)
        recent_orders = cls.objects.filter(order_date__gte=six_months_ago)

        top_customers = (
            recent_orders
            .values('customer__id', 'customer__username')
            .annotate(total_spent=models.Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
        return top_customers
