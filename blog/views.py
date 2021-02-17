from django.shortcuts import render
from . import models as m

def home(request):
    data = m.Post.objects.all()
    context = {'posts': data}
    return render(request, 'blog/index.html', context=context)

def about(request):
    return render(request, 'blog/about.html')

