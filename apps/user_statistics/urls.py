from django.urls import path, include
from .views import GenderStatistics, AgeStatistics, BoardGenderStatistics, BoardAgeStatistics
# from .views import LoginStatistics

urlpatterns=[
    path('user/gender',GenderStatistics.as_view()),
    path('user/age',AgeStatistics.as_view()),
    # path('user/login',LoginStatistics.as_view()),
    path('board/gender', BoardGenderStatistics.as_view()),
    path('board/age',BoardAgeStatistics.as_view())
]
