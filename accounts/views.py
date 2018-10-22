# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'