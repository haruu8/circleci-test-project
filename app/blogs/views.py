from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

class SampleView(generic.TemplateView):
    template_name = 'blogs/sample.html'
