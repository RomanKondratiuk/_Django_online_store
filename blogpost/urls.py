from django.urls import path

from blogpost.apps import BlogpostConfig
from blogpost.views import BlogpostCreateView, BlogPostListView, BlogPostDetailView, BlogpostUpdateView, \
    BlogPostDeleteView, toggle_activity

app_name = BlogpostConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogpostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
    # path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

]

