
from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),

]
