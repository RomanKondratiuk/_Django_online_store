from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogpost.models import BlogPost


class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')


class BlogpostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')
