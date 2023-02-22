from django.urls import path, include
from .views import LogExport
# from .views import LoginStatistics

urlpatterns=[
    path('',LogExport.as_view()),
]
