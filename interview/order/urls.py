
from django.urls import path
from interview.order.views import (
    OrderListCreateView, 
    OrderTagListCreateView, 
    OrderListEmbargoDatesView)


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('embargo/', OrderListEmbargoDatesView.as_view(), name='order-embargo-list'),
]