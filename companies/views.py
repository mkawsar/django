from .models import Companies
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexListView(LoginRequiredMixin, generic.ListView):
    template_name = 'companies/index.html'
    model = Companies

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['title'] = 'Company List'
        return context
