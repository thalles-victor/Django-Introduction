
from django.urls import path
from view.views import getInformation
urlpatterns = [
    path('informations/<str:id>', getInformation),
]
