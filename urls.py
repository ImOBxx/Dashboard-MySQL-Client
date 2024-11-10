from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('update-sales/', views.update_sales, name='update_sales'), 
    path('api/sales-data/', views.sales_data_api, name='sales-data-api'), 
    path('sales-histogram/', views.sales_histogram, name='sales_histogram'),
]
