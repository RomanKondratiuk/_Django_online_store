from django.urls import path

from blogpost.apps import BlogpostConfig
from blogpost.views import BlogpostCreateView, BlogPostListView

app_name = BlogpostConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('', BlogPostListView.as_view(), name='list'),
    # path('view/<int:pk>', ..., name='view_blogpost '),
    # path('edit/<int:pk>/', BlogpostUpdateView.as_view(), name='update_blogpost'),
    # path('delete/<int:pk>/', BlogpostDeleteView.as_view(), name='delete_blogpost'),


]

