from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog_all'),
    path('catalog/<slug:category_slug>/', views.CatalogView.as_view(), name='catalog'),
    path('service/<slug:slug>', views.ServiceDetailView.as_view(), name='service_detail'),
]

