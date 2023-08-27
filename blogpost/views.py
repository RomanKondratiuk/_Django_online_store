from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blogpost.models import BlogPost


class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost
