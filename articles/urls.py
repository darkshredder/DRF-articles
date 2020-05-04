
from django.urls import path, include
#from .views import article_list, article_detail
from .views import ArticleDetail, ArticleList
urlpatterns = [

    #path('', article_list ),
    #path('<int:pk>/', article_detail),
    path('', ArticleList.as_view()),
    path('<int:pk>/', ArticleDetail.as_view()),
    ]
