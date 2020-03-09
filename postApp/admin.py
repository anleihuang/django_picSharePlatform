from django.contrib import admin
from postApp.models import User, Friendship, Post, Like, Comment


admin.site.register(User)
admin.site.register(Friendship)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
