from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'terminaux_perdus'
urlpatterns = [
    path('create/',views.Create),
    path('edit/<ticket_id>',views.Edit),
]
