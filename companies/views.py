from .models import Companies
from django.views import generic
from django.contrib import messages
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
class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Companies
    fields = ['name', 'description', 'location', 'motto', 'type', 'picture']
    template_name = 'companies/add.html'
    success_url = '/company/list'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, 'Company information created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create company information!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Company Create'
        return context


# Company information delete view
@login_required()
def delete(request, id):
    try:
        company = Companies.objects.get(pk=id)
        company.delete()
        messages.success(request, 'Company information delete successfully!')
        return redirect('company:list')
    except Companies.DoesNotExist:
        messages.error(request, 'Company information does not exist!')
        return redirect('company:list')
    except Exception as e:
        print(e)
        messages.error(request, 'Failed to delete company information!')
        return redirect('company:list')
