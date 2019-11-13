from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

from .serializers import BookmarkSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
class ApiBookmarkList(ListAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer
class ApiBookmarkDetail(RetrieveUpdateDestroyAPIView):
   queryset = Bookmark.objects.all()
   serializer_class = BookmarkSerializer

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by =  3


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

