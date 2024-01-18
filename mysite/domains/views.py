from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Domain

class IndexView(generic.ListView):
    template_name = "domains/index.html"
    context_object_name = "domain_list"

    def get_queryset(self):
        """
        Return a list of domains.
        """
        return Domain.objects.all()

class DetailView(generic.DetailView):
    model = Domain
    template_name = "domains/detail.html"