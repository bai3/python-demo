from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Post, User
from django.template.loader import get_template
from datetime import datetime
# from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
        else:
            raise Http404('无信息')
    except:
        raise Http404('无信息')


def login(request):
    template = get_template('login.html')
    try:
        username = request.GET['username']
        password = request.GET['password']
    except:
        username = None
        password = None
    html = template.render(locals())

    return HttpResponse(html)

