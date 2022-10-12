from django.shortcuts import render

from . import models


def index(request):
    post = models.Post.objects.order_by('?').first()
    return render(request, 'post.html', context={'post': post})
