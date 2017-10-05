from django.shortcuts import render
from django.views.decorators import csrf


def search_post(resquest):
    ctx = {}
    if resquest.POST:
        ctx['rlt'] = resquest.POST['q']
    return render(resquest, "post.html", ctx)
