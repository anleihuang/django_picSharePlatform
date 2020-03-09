from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# TABLE Name: User
# Columns: id (default, PK), profile_pic, email


class User(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to="profiles",
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("usrprofile", args=[str(self.id)])

    def get_friends(self):
        friendship = Friendship.objects.filter(user=self)
        return friendship

    def get_followers(self):
        followers = Friendship.objects.filter(following=self)
        return followers


# TABLE Name: Friendship
# Columns: id (default, PK), user, following, created_date
class Friendship(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_user_set"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friendship_following_set"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.username + " follows " + self.following.username


# TABLE Name: Post
# Columns: id (default, PK), user, image, comment, created_date
class Post(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE, related_name="posts"
    )
    image = ProcessedImageField(
        upload_to="posts",
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def get_like_count(self):
        return self.likes.count()

    def get_comment_count(self):
        return self.comments.count()


# TABLE Name: Like
# Columns: id (default, PK), user, post,
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    # restrict only generating one unique record
    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return self.user.username + " likes post #" + str(self.post.pk)


# TABLE Name: Comment
# Columns: id (default, PK), user, post, comment, created_date
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment
