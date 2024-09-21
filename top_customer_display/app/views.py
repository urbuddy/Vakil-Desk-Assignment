from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    '''
    View to manage the request to display top most 5 users
    :param request: user's request and data
    :return: Template to display the data and top_customers data
    '''
    top_customers = Order.top_5_customers()
    return render(request, 'top_customers.html', {'top_customers': top_customers})
