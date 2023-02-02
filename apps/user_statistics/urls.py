from django.urls import path, include
from .views import GenderStatistics, AgeStatistics, LoginStatistics

urlpatterns=[
    path('user/gender',GenderStatistics.as_view()),
    path('user/age',AgeStatistics.as_view()),
    path('user/login',LoginStatistics.as_view()),
]
