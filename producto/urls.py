from django.urls import path
from .views import Producto, ProductoDetalle
from .models import Producto as MProducto

urlpatterns = [
    path('', Producto.as_view(), name='productos' ),
    path('<int:pk>', ProductoDetalle.as_view(model=MProducto), name="detalle"),
]