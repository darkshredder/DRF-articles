
from django.urls import path, include
from .views import article_list, article_detail
urlpatterns = [

    path('', article_list ),
    path('<int:pk>/', article_detail),
    ]
