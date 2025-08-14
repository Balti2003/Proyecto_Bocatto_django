from django.urls import path
from .views import ProductsByCategoryView, ProductListView, ProductDetailView

urlpatterns = [
    path('category/<categoria_id>/', ProductsByCategoryView.as_view(), name='productos_por_categoria'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path("products/<pk>/", ProductDetailView.as_view(), name="product_detail"),
]
