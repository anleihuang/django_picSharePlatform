# referenced by: https://github.com/yibeibaoke

"""
to create three customed tags so the function can be called in web
1. return if the people viewing is followed by the current viewer (user)
2. to toggle the like button
3. 
"""

from django import template
from django.urls import reverse, NoReverseMatch
from postApp.models import Like

import re

register = template.Library()


@register.simple_tag
def is_following(user, following):
    return following.get_followers().filter(user=user).exists()


@register.simple_tag
def toggle_like(user, post):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-hand-peace-o"
    except:
        return "fa-hand-rock-o"


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context["request"].path
    if re.search(pattern, path):
        return "active"
    return ""
