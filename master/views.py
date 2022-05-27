from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View, DetailView
from django.core.mail import send_mail
from django.conf import settings
from master.models import ContactUs


from product.models import CartModel, ProductModel , CategoryModel
from master.forms import ContactForm
# Create your views here.


# context for title


# def home_view(request):
#     template_name = 'master/home.html'
#     context = {
#         'title':'home'
#     }

#     return render (request,template_name, context)


'''def hello_world(request):
    return HttpResponse("<h1> HELLO WORLD </h1>")'''

# def about_us(request):
#     template_name = 'master/aboutus.html'
#     context = {
#         'title':'aboutus'
#     }
#     return render (request,template_name,context)


# def contact_us(request):
#     template_name = 'master/contactus.html'
#     context = {
#         'title':'aboutus'
#     }

#     return render(request,template_name,context)


# class based views

class HomeView(TemplateView):
    template_name = 'master/home.html'
   
    extra_context = {
        'title': 'home',
        'products' : ProductModel.objects.all(),
        'category' : CategoryModel.objects.all(),
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cart'] = CartModel.objects.filter(user=self.request.user).last()
    #     return context


class AboutUsView(TemplateView):
    template_name = 'master/aboutus.html'
    extra_context = {
        'title': 'about us'
    }


class ContactUsView(View):
    template_name = 'master/contactus.html'
    form_class = ContactForm
    def get(self,request):

        context = {
            'title': 'contact us',
            'form' : self.form_class
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('contactus'))
        

    def form_valid(self, form):
        data = form.cleaned_data
        from_email = settings.EMAIL_HOST_USER
        to_email = data['email']
        name = data['name']
        subject = data['subject']
        message = data['message']

        contact_obj = ContactUs.objects.create(
            name=name,
            email = to_email,
            subject = subject,
            message = message
        )
        
        # sending email
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_email, 
            recipient_list=[to_email]
            )

        print("Mail sent successfully!!")

    def form_invalid(self, form):
        context = {
            "form" : form
        }
        return render(self.request, self.template_name, context)

class ContactedList(View):
    template_name = 'master/contactusemail.html'
    def get(self,request):
        context={
            "emails":ContactUs.objects.all()
        }
        return render (request,self.template_name,context)

class ContactUsSendReply(View):
    template_name = 'master/contactus/send_reply.html'
    form_class = ContactForm
    def get(self,request, pk):
        context={
            'form':self.form_class
        }
        return render(request,self.template_name,context)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)
        self.object = ContactUs.objects.get(id=pk)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return redirect(reverse_lazy('contactus_list'))
        

    def form_valid(self, form):
        data = form.cleaned_data
        from_email = settings.EMAIL_HOST_USER
        to_email = self.object.email
        name = data['name']
        subject = data['subject']
        message = data['message']
        
        # sending email
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_email, 
            recipient_list=[to_email]
            )

        print("Mail sent successfully!!")

        self.object.reply = message
        self.object.is_replied = True
        self.object.save()

    def form_invalid(self, form):
        context = {
            "form" : form
        }
        return render(self.request, self.template_name, context)


class ContactUsReply(DetailView):
    template_name = 'master/contactus/view_reply.html'
    model = ContactUs