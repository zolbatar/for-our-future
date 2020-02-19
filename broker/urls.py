from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company', views.get_company, name='get_company'),
]