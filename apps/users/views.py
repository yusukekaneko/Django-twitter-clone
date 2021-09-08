from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('apps.users:login')
    template_name = 'registration/signup.html'

