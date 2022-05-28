import requests
from django.shortcuts import render,redirect 
from django.conf import settings
from django.views.generic import (
    ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, 
    View, RedirectView
    )
from django.urls import reverse_lazy
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import ProfileForm, UserForm
from user.models import ProfileModel

from user.forms import LoginForm


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

class DashboardView(LoginRequiredMixin, View):
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



# def login(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
          
#         if form.is_valid():
#             return render(request,self.template_name,context)
#         else:
#             return HttpResponse("OOPS! Bot suspected.")
            
#     else:
#         form = ContactForm()
          
#     return render(request, 'login.html')


class LoginView(View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        context={
            'form':self.form_class()
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
                self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('dashboard'))

    def form_valid(self, form):
        user = None
        data = form.cleaned_data
        username = data['username']
        password = data['password']

        # recaptch verification
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        url = settings.GOOGLE_RECAPTCHA_VERIFY_URL
        #  API call to google API's to validate recaptcha response
        data = requests.post(url, data=values).json()
       
        if data['success']:
            user = authenticate(self.request, username=username, password=password)
        if user is None:
            return self.form_invalid(form)
        login(self.request, user)

    def form_invalid(self, form):
        context = {
            'form' :form
        }
        return render(self.request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home'))




