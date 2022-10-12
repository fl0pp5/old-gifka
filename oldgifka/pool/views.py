from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.


def index(request):
    post = models.Post.objects.order_by('?').first()
    return render(request, 'post.html', context={'post': post})
