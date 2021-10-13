from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import ListView

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        print("request recieved")
        total = form.cleaned_data.get('total')
        print("here")
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        print("request processed")
        return redirect('users_list')


class UserListView(ListView):
    model = User
    template_name = "core/user_list.html"

    