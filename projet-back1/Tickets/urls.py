from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'ticketing'
urlpatterns = [
    path('create/',views.Create),
    path('edit/<ticket_id>',views.Edit),
    path('', views.home)
]
