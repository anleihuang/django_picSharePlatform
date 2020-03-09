# create urls.py in subfolder to manage the route urls to view

"""djangodemo URL Configuration

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
from postApp.api_views import (
    APIPostListExploreView,
    APIPostPostExploreView,
    APIPostDetailView,
)
from postApp.api_views import APIUserSignUp, APIUserGetProfile

urlpatterns = [
    path(
        "post", APIPostListExploreView.as_view(), name="api_get_post"
    ),  # GET /api/v1/postApp/post/
    path(
        "post/create/", APIPostPostExploreView.as_view(), name="api_create_post"
    ),  # POST /api/v1/postApp/post/create/
    path(
        "post/update/<int:pk>/", APIPostDetailView.as_view(), name="api_gpd_post"
    ),  # GET PUT DELETE /api/v1/postApp/update/<id>/
    path("auth/signup", APIUserSignUp.as_view(), name="api_signup"),
    path(
        "user/get_profile/<int:pk>/",
        APIUserGetProfile.as_view(),
        name="api_get_usrprofile",
    ),  # PUT /api/v1/postApp/user/get_profile/<id>/
]
