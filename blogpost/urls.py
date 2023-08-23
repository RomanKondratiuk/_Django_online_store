from django.urls import path

from blogpost.apps import BlogPostConfig
from blogpost.views import BlogpostCreateView

app_name = BlogPostConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    # path('read/', ..., name='read'),
    # path('update/<int:pk>/', ..., name='update'),
    # path('delete/<int:pk>/', ..., name='delete')

]

