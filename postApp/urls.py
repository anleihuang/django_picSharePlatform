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
from postApp.views import PostListView, PostExploreView, PostDetailView
from postApp.views import PostCreateView, PostUpdateView, PostDeleteView
from postApp.views import UserSignUp, UserProfile, UserUpdateProfile
from postApp.views import addComment, addLike, followToggle

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("explore", PostExploreView.as_view(), name="explore"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("post/create/", PostCreateView.as_view(), name="create_post"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="update_post"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="delete_post"),
    path("auth/signup", UserSignUp.as_view(), name="signup"),
    path("user/profile/<int:pk>/", UserProfile.as_view(), name="usrprofile"),
    path(
        "user/update_profile/<int:pk>/",
        UserUpdateProfile.as_view(),
        name="update_usrprofile",
    ),
    path("like", addLike, name="addLike"),
    path("comment", addComment, name="addComment"),
    path("followToggle", followToggle, name="followToggle"),
]
