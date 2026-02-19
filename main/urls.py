from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('service/<slug:slug>', views.ServiceDetailView.as_view(), name='service_detail'),
]

