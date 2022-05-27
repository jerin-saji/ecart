from django.urls import path

# from master.views import AboutUs, HomeView, about_us, hello_world, home_view, contact_us
from master.views import (ContactUsView, 
HomeView, AboutUsView,
ContactedList, ContactUsSendReply,ContactUsReply
)


urlpatterns = [

    # path("",home_view,name="home"),
    # path("hello_world",hello_world,name="hello_world"),
    # path("aboutus/",about_us,name="about_us"),
    # path("contactus/",contact_us,name="contact_us")

    path("", HomeView.as_view(), name='home'),
    path("contactus/", ContactUsView.as_view(), name='contactus'),
    path("aboutus/", AboutUsView.as_view(), name='aboutus'),
    path("contactus/list", ContactedList.as_view(), name='contactus_list'),
    path("contactus/<int:pk>/send", ContactUsSendReply.as_view(), name='contactus_send_reply'),
    path("contactus/<int:pk>/reply", ContactUsReply.as_view(), name='contactus_view_reply'),

]
