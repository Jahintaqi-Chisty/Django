from django.urls import path
from . import views



#Creating views
app_name = 'contact'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contact_app', views.contact_list, name='contact_list'),
    path('contact_app/person/<int:pk>', views.contact_detail, name='contact_detail'),
    path('contact_app/person/new', views.contact_new, name='contact_new'),
    path('contact_app/person/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('contact_app/person/<int:pk>/delete', views.contact_delete, name='contact_delete'),
    ]