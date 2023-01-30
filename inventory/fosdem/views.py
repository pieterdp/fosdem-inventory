from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Box

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'fosdem/boxes.html'
    context_object_name = 'all_boxes'

    def get_queryset(self):
        return Box.objects.all()


class DetailView(generic.DetailView):
    model = Box
    template_name = 'fosdem/box.html'

