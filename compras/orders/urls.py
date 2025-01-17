from django.urls import path
from django.contrib import admin
from compras.orders.views import (
    create_order,
    View_producer,
)


app_name = "orders"
urlpatterns = [
    path("create/", view=create_order, name="create"),
    path("producer/<int:pk>", view=View_producer.as_view(), name="producer"),
]

