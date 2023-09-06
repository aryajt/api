from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_device,name="create_device"),
    path('get-device/', views.get_device,name="get_device"),
    path('all/', views.get_all_devices),
]
