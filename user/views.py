from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, View
from django.urls import reverse_lazy

from user.forms import ProfileForm, UserForm
from user.models import ProfileModel


# Create your views here.
# Profile
class ProfileView(DetailView):
    template_name = "profile/profile.html"
    model = ProfileModel

    def get_queryset(self):
        queryset = ProfileModel.objects.get(user=self.request.user)
        return queryset

class ProfileCreateView(CreateView):
    template_name = 'user/profile/create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

# User
class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserForm
    success_url = reverse_lazy('home')


# class DashboardView(TemplateView):
#     template_name = 'user/dashboard.html'

class DashboardView(View):
    template_name = 'user/dashboard.html'

    def get(self, request):
        profile = self.get_queryset()
        context = {
            'profile' : profile
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass

    def get_queryset(self):
        queryset = ProfileModel.objects.filter(user=self.request.user).first()
        return queryset



