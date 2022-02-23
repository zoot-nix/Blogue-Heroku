from blogueApp.models import Profile
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from members.forms import SignUpForm
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import ChangePasswordForm, CreateBioForm, EditBioForm, SignUpForm, EditUserForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args , **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')

class EditBioView(generic.UpdateView):
    model = Profile
    form_class = EditBioForm
    template_name = 'registration/edit_bio.html'
    success_url = reverse_lazy('home')

class CreateBioView(CreateView):
    model = Profile
    form_class = CreateBioForm
    template_name = "registration/create_bio.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
