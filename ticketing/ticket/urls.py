from django.urls import path
from ticket import views

urlpatterns = [
    path('tickets', views.ticket_list),
    path('ticket/<str:pk>', views.ticket_detail),
    path('idClient', views.client),
    path('idService', views.service),
]