from .models import Companies
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class IndexListView(LoginRequiredMixin, generic.ListView):
    template_name = 'companies/index.html'
    model = Companies
    context_object_name = 'companies'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Company List'
        return context

# Create a company information
@login_required
def create(request):
    return render(request, 'companies/add.html', {'title': 'Company Create'})
