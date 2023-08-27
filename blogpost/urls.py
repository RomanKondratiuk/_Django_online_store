from django.urls import path

from blogpost.apps import BlogpostConfig

app_name = BlogpostConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create_blogpost'),
    # path('', ..., name='list'),
    # path('view/<int:pk>', ..., name='view_blogpost '),
    # path('edit/<int:pk>/', BlogpostUpdateView.as_view(), name='update_blogpost'),
    # path('delete/<int:pk>/', BlogpostDeleteView.as_view(), name='delete_blogpost'),


]

