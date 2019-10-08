from django.shortcuts import render ,redirect
from .models import CustomUser
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm,CustomerSignUpForm,CompanySignUpForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomerSignUpView(generic.CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        
        return redirect('login')

class CompanySignUpView(generic.CreateView):
    model = CustomUser
    form_class = CompanySignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        
        return redirect('login')