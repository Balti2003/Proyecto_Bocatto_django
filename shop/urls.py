from django.urls import path
from .views import MercadoPagoInitView, PaymentFailureView, PaymentSuccessView, ProductsByCategoryView, ProductListView, ProductDetailView, CartView, AddToCartView, ProductDeleteView
from .views import RemoveFromCartView, CheckoutView, OrderDetailView, OrderListView, PasswordChangeView, PasswordChangeDoneView, ProductCreateView, ProductUpdateView, ProductManageListView 

urlpatterns = [
    path('category/<categoria_id>/', ProductsByCategoryView.as_view(), name='productos_por_categoria'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path("products/<pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("cart/", CartView.as_view(), name="carrito"),
    path("cart/add/<int:producto_id>/", AddToCartView.as_view(), name="agregar_al_carrito"),
    path("cart/remove/<int:producto_id>/", RemoveFromCartView.as_view(), name="eliminar_del_carrito"),
    path("cart/checkout/", CheckoutView.as_view(), name="checkout"),
    path("order/<pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("my_orders/", OrderListView.as_view(), name="order_list"),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path("product/new/", ProductCreateView.as_view(), name="product-create"),
    path("manage/products/", ProductManageListView.as_view(), name="product-manage"),
    path("manage/product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product-update"),
    path("manage/product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("pedido/<int:pk>/pagar/", MercadoPagoInitView.as_view(), name="order_pay"),
    path("pago/success/", PaymentSuccessView.as_view(), name="payment_success"),
    path("pago/failure/", PaymentFailureView.as_view(), name="payment_failure"),
]
