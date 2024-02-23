from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet, DashboardViewSet, ItemViewSet, OrderViewSet, OrderCreateView, add_phone_number

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'orders', OrderViewSet, basename='order')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', HomeViewSet.as_view({'get': 'list'}), name='home'),
    path('dashboard/', DashboardViewSet.as_view({'get': 'list'}), name='dashboard'),
    # path('items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list-create'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),  # Endpoint for creating orders manually defined
    path('', include(router.urls)),  # Includes all registered routes
    path('add_phone_number/', add_phone_number, name='add_phone_number'),
]
