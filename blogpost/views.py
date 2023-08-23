from django.shortcuts import render
from django.views.generic import CreateView

from blogpost.models import BlogPost


class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)

