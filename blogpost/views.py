from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blogpost.models import BlogPost


class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

            return super().form_valid(form)



class BlogpostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_publication=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')
