# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article

def index(request):
    context = {
        'article': Article.objects.order_by('-created')
    }
    return render(request, 'myapp/index.html', context)
