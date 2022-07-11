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
    path('about/', views.IndexView.as_view()),
    path('structure/', views.StrucView.as_view()),
    path('today/', views.TimeView.as_view()),
    path('directors/', views.DirectorListView.as_view()),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view()),
    path('movies/', views.MovieListView.as_view()),
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),
    path('reviews/', views.ReviewListView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),
    path('director/<int:director_id>/movies/', views.DirectorMovieFilterView.as_view()),
    path('movie/<int:movie_id>/reviews/', views.MovieReviewFilterView.as_view()),
    path('add_director/', views.AddDirectorFormView.as_view()),
    path('add_movie/', views.AddMovieFormView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view())

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)