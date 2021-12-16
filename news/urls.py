"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import bot,NewsList,NewsDetail,NewsListView,NewsDetailView,NewsListFiltered

urlpatterns = [
    path('bot/', bot, name='bot' ),  
    path('newsapi/', NewsList.as_view(), name='newslist' ), 
    path('newsapi/<str:title>', NewsListFiltered.as_view(), name='newslist' ),
    path('newsapi/d/<int:pk>', NewsDetail.as_view(), name='newsdetail' ),
    path('news/', NewsListView, name='news'),
    path('news/<int:page>', NewsListView, name='news'),
    path('news/d/<int:_id>', NewsDetailView, name='news_d'),    
]