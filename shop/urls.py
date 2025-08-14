from django.urls import path
from .views import ProductsByCategoryView, ProductListView, ProductDetailView, CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('category/<categoria_id>/', ProductsByCategoryView.as_view(), name='productos_por_categoria'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path("products/<pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("cart/", CartView.as_view(), name="carrito"),
    path("cart/add/<int:producto_id>/", AddToCartView.as_view(), name="agregar_al_carrito"),
    path("cart/remove/<int:producto_id>/", RemoveFromCartView.as_view(), name="eliminar_del_carrito"), 
]
