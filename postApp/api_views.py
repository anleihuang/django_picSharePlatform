## Import Libs
# rest api serializer
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from postApp.serializers import UserSerializer, PostSerializer

# customed templates
from postApp.models import User, Post  # ,Friendship, Like, Comment


### CRUD Posts - API


class APIPostListExploreView(generics.ListAPIView):
    """
    GET post/
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class APIPostPostExploreView(generics.CreateAPIView):
    """
    POST post/
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        super(APIPostPostExploreView, self).create(request, args, kwargs)
        response = {
            "status_code": status.HTTP_201_CREATED,
            "message": "Success",
            "result": request.data,
        }
        return Response(response)


class APIPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET post/:id/
    PUT post/:id/
    DELETE post/:id/
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        super(APIPostDetailView, self).get(request, args, kwargs)
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Success",
            "result": data,
        }
        return Response(response)

    def put(self, request, *args, **kwargs):
        super(APIPostDetailView, self).put(request, args, kwargs)
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Success",
            "result": data,
        }
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(APIPostDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_204_NO_CONTENT, "message": "Success"}
        return Response(response)


class APIUserSignUp(generics.CreateAPIView):
    """
    POST user/signup
    """

    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        username = request.query_params.get("username", None)
        password = request.query_params.get("password", None)
        first_name = request.query_params.get("first_name", None)
        last_name = request.query_params.get("last_name", None)
        email = request.query_params.get("email", None)
        if not username or not password or not first_name or not last_name or not email:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "username, password, first_name, last_name and email \
                            are all required",
            }
            return Response(response)
        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        response = {
            "status_code": status.HTTP_201_CREATED,
            "message": "Success",
            "result": UserSerializer(new_user).data,
        }
        return Response(response)


class APIUserGetProfile(generics.RetrieveUpdateDestroyAPIView):
    """
    GET user/update_profile/:id/
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        super(APIUserGetProfile, self).get(request, args, kwargs)
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Success",
            "result": data,
        }
        return Response(response)
