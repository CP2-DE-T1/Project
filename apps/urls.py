from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('boards/', include('apps.boards.urls')),
    path('statistics/', include('apps.user_statisics.urls'))
]