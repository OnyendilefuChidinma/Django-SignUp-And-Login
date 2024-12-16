from django.urls import path
from .views import Bloghome, Post_list, contact_success, contact_view
from .about import About_us, Contact_us
from .post_detailsview import post_details


urlpatterns = [
    path('',Bloghome,name='home' ),
    path('about_us/', About_us, name='aboutus'),
    path('contact_us/', Contact_us, name='contactus'),
    path('post_list', Post_list, name='post'),
    path('<int:post_id>/', post_details, name="details"),
    
    path('contact_us/contact_view', contact_view, name='contact_form'),
    # path('success/', success, name='success'),
    path('contact_us/contact_view/success/', contact_success, name='success_message')

]
