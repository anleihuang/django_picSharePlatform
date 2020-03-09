from rest_framework import serializers

from postApp.models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "date_joined",
            "last_login",
            "username",
            "profile_pic",
            "first_name",
            "last_name",
            "email",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
