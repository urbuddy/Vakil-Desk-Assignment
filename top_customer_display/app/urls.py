from django.urls import path
from .views import top_customers_view

# request url's
urlpatterns = [
    path('', top_customers_view, name='top_customers'),
]