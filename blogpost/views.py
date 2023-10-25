from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blogpost.models import BlogPost


class BlogpostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

            return super().form_valid(form)


class BlogpostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    # success_url = reverse_lazy('blogpost:list')

    def get_success_url(self):
        return reverse('blogpost:view', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

            return super().form_valid(form)


class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_publication=True)
        # queryset = queryset.filter(sign_publication=False)
        return queryset


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')


def toggle_activity(request, pk):
    post_item = get_object_or_404(BlogPost, pk=pk)
    if post_item.sign_publication:
        post_item.sign_publication = False
    else:
        post_item.sign_publication = True

    post_item.save()

    return redirect(reverse('blogpost:list'))
