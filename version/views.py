from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from version.forms import VersionForm
from version.models import Version


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(version_status=True)
        return queryset


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('version:version_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('version:version_list')


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('version:version_list')


class VersionDetailView(DetailView):
    model = Version

    def __str__(self):
        return self.object
