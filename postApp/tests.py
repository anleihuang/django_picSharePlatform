# from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase

from rest_framework.views import status

from postApp.models import User, Post


class APIPostPostExploreView(APITestCase):
    """Test the APIPostPostExploreView view class
    POST post/ """

    def setUp(self):
        """set up url: /api/v1/post/update/{pk}/"""
        self.url = reverse("api_create_post", kwargs={"version": "v1"})

    def test_get_post_detail(self):
        data = {"comment": "test_comment_1"}
        response = self.client.post(self.url, data=data, format="json")
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.post_test = Post.objects.first()
        # test the content
        self.assertEqual(data["comment"], self.post_test.comment)


class APIPostDetailView(APITestCase):
    """Test the APIPostDetailView view class
    GET post/:id/
    PUT post/:id/
    DELETE post/:id/
    """

    def setUp(self):
        """set up url: /api/v1/post/update/{pk}/"""
        self.post_test = Post(comment="test_comment_2")
        self.post_test.save()
        self.url = reverse(
            "api_gpd_post", kwargs={"version": "v1", "pk": self.post_test.pk}
        )

    def test_get_pk_detail(self):
        response = self.client.get(self.url)
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        # test the content
        self.assertEqual(data["result"]["comment"], self.post_test.comment)

    def test_put_pk_detail(self):
        response = self.client.put(
            self.url, data={"comment": "new_comment"}, format="json"
        )
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # refresh the database after update
        self.post_test.refresh_from_db()
        # test the content
        self.assertEqual(self.post_test.comment, "new_comment")

    def test_delete_pk_detail(self):
        # the count of the object should be 1
        self.assertEqual(Post.objects.count(), 1)

        response = self.client.delete(self.url)
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # the count of the object should be 0 after deleting it
        self.assertEqual(Post.objects.count(), 0)


class APIUserSignUp(APITestCase):
    """Test the APIUserSignUp view class
    POST user/signup
    """

    def setUp(self):
        """set up url: /api/v1/user/signup"""
        self.url = reverse("api_signup", kwargs={"version": "v1"})

    def test_create(self):
        data = {
            "username": "test_user",
            "password": "password",
            "first_name": "test_first",
            "last_name": "test_last",
            "email": "test@email"
        }

        response = self.client.post(self.url, data=data, format="json")
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class APIUserGetProfile(APITestCase):
    """Test the APIUserGetProfile view class
    GET user/update_profile/:id/
    """

    def setUp(self):
        """set up url: user/update_profile/:id/"""
        self.user_test = User(
            username="test_user",
            password="password",
            first_name="test_first",
            last_name="test_last",
            email="test@email",
        )
        self.user_test.save()
        self.url = reverse(
            "api_get_usrprofile", kwargs={"version": "v1", "pk": self.user_test.pk}
        )

    def test_get(self):
        response = self.client.get(self.url)
        # test the connection success
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        # test the content
        self.assertEqual(data['result']['username'], self.user_test.username)
        self.assertEqual(data['result']['first_name'], self.user_test.first_name)
        self.assertEqual(data['result']['last_name'], self.user_test.last_name)
        self.assertEqual(data['result']['email'], self.user_test.email)
