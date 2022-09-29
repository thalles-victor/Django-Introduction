from django.urls import path
from tasks.views import helloworld

urlpatterns = [
    path('helloworld/', helloworld),
]
