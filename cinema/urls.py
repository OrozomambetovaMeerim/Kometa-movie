"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
    path('films/', films, name="films"),
    path('rating/', rating, name="rating"),
    path('contact/', contact, name="contact"),
    path('base/', base, name="base"),
    path('show/', show, name="show"),
    path('movies/', movies, name='movies'),
    path('create/', create_movie, name='create-movie'),
    path('<int:id>/', movie, name='movie'),
    path('<int:id>/edit/', edit_movie, name='edit-movie'),
    path('<int:id>/delete', delete_movie, name='delete-movie'),
    path('news/', news, name="news"),
    path('kabar/', kabar, name="kabar"),
    path('news_2/', news_2, name="news_2"),
    path('search/', search, name='search_field'),
    path('message/', message, name="reviews"),
    path('<int:id>/get_message/', DialogsViews.as_view(), name='message'),
    # path("login/", login, name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
