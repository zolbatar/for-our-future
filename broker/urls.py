from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    # Company - list, entry
    path(r'company', views.CompanyList),
    path(r'company/entry', views.CompanyEntry),
]
