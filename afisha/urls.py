"""afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.index),
    path('structure/', views.structure),
    path('today/', views.presenttime),
    path('directors/', views.director_list_view),
    path('directors/<int:id>/', views.director_detail_view),
    path('movies/', views.movie_list_view),
    path('movies/<int:id>/', views.movie_detail_view),
    path('reviews/', views.review_list_view),
    path('reviews/<int:id>/', views.review_detail_view),
    path('director/<int:director_id>/movies/', views.director_movie_filter_view),
    path('movie/<int:movie_id>/reviews/', views.movie_review_filter_view),
    path('add_director/', views.add_director_view),
    path('add_movie/', views.add_movie_view),
    path('register/', views.register_view),
    path('login/', views.login_view),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)