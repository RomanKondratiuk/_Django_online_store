from django.urls import path

from version.apps import VersionConfig
from version.views import VersionCreateView, VersionUpdateView, VersionListView, VersionDeleteView, VersionDetailView

app_name = VersionConfig.name

urlpatterns = [
    path('', VersionListView.as_view(), name='version_list'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='view_version'),
    path('create/', VersionCreateView.as_view(), name='create_version'),
    path('update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),



]

