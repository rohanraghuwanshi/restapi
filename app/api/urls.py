from django.urls import path

from .views import *

urlpatterns = [
    path('', StatusListAPIView.as_view()),
    path('search/', StatusListSearchAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    path('detail/<int:pk>/', StatusDetailAPIView.as_view()),
    path('update/<int:pk>', StatusUpdateAPIView.as_view()),
    # path('delete/<int:pk>/', StatusDeleteAPIView.as_view()),
]
