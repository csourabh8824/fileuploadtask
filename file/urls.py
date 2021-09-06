from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileDownload.as_view(), name='homepage'),
]
