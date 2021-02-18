from django.shortcuts import render
from . import models as m
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    data = m.Post.objects.all()
    context = {'posts': data}
    return render(request, 'blog/index.html', context=context)


@login_required
def about(request):
    return render(request, 'blog/about.html')

