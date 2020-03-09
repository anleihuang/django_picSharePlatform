## Import Libs
# fullfill master-detail interface
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# import django utiliy
from django.urls import reverse_lazy

# import django authentication system
from django.contrib.auth.mixins import LoginRequiredMixin

#
from annoying.decorators import ajax_request


# customed templates
from postApp.models import User, Post, Friendship, Like, Comment
from postApp.forms import CustomUserCreationForm


### CRUD Posts


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "index.html"
    login_url = "login"

    # overwrite get_queryset
    # shown only following's posts
    def get_queryset(self):
        user = self.request.user
        following_set = set()
        for friend in Friendship.objects.filter(user=user).select_related("following"):
            following_set.add(friend.following)
        return Post.objects.filter(user__in=following_set)


class PostExploreView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "explore.html"
    login_url = "login"

    # overwrite get_queryset
    def get_queryset(self):
        return Post.objects.all().order_by("-created_date")[:50]


class PostDetailView(DetailView):
    model = Post
    template_name = "detail_post.html"

    # overwrite get_context_data
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes = Like.objects.filter(
            post=self.kwargs.get("pk"), user=self.request.user
        ).first()
        if likes:
            data["likes"] = 1
        else:
            data["likes"] = 0
        return data


class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = "__all__"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["comment"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("index")


### User


class UserSignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"
    login_url = "login"


class UserUpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "update_profile.html"
    fields = ["profile_pic", "username"]
    login_url = "login"


### Ajax
@ajax_request
def addLike(request):
    post_pk = request.POST.get("post_pk")
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(user=request.user, post=post)
        like.save()
        result = 1
    except:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        result = 0

    return {"post_pk": post_pk, "result": result}


@ajax_request
def addComment(request):
    post_pk = request.POST.get("post_pk")
    comment = request.POST.get("comment")
    post = Post.objects.get(pk=post_pk)
    info = {}
    try:
        username = request.user.username
        comment = Comment(user=request.user, post=post, comment=comment)
        comment.save()
        info = {"username": username, "comment": comment}
        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {"post_pk": post_pk, "result": result, "info": info}


@ajax_request
def followToggle(request):
    user = User.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get("follow_user_pk")
    following = User.objects.get(pk=follow_user_pk)
    try:
        if user != following:
            if request.POST.get("type") == "following":
                friendship = Friendship(user=user, following=following)
                friendship.save()
            elif request.POST.get("type") == "unfollowed":
                Friendship.objects.filter(user=user, following=following).delete()
            result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        "follow_user_pk": follow_user_pk,
        "type": request.POST.get("type"),
        "result": result,
    }
