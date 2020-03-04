from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post


def post_list(request):
    me = User.objects.all()[0]
    posts = Post.objects.filter(author=me)
    return render(request, 'blog/post_list.html', {'posts': posts})

