""
from django.urls import  path
from . import views

urlpatterns=[
    # path('article/',views.article_list,name='article'),
    path('article/',views.ArticleAPIView.as_view(),name='article'),
    path('detail/<int:pk>',views.article_detail,name='detail'),
]