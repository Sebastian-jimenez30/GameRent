from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.transactions.views import AddToCartView, CartView, RemoveFromCartView, UpdateCartItemTypeView, CheckoutCartView, UpdateCartItemSharedUsersView, RemoveSharedUserFromCartItemView

from .views import (
    RentalViewSet,
    PurchaseViewSet,
    SharedRentalViewSet,
    SharedRentalPaymentViewSet,
    CartViewSet,
    CartItemViewSet,
    InvoiceViewSet,
    PaymentViewSet
)

router = DefaultRouter()
router.register(r'rentals', RentalViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'shared-rentals', SharedRentalViewSet)
router.register(r'shared-rental-payments', SharedRentalPaymentViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/update-type/<int:item_id>/', UpdateCartItemTypeView.as_view(), name='update_cart_item_type'),
    path('cart/checkout/', CheckoutCartView.as_view(), name='checkout_cart'),
    path('cart/update-shared-users/<int:item_id>/', UpdateCartItemSharedUsersView.as_view(), name='update_shared_users'),
    path('cart/remove-shared-user/<int:item_id>/<int:user_id>/', RemoveSharedUserFromCartItemView.as_view(), name='remove_shared_user'),
]
