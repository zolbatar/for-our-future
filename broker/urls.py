from django.urls import path
from . import views

app_name = 'broker'

urlpatterns = [
    path('', views.index),

    # Company - list, entry
    path('company', views.CompanyList),
    path('company/<int:company_id>/delete', views.CompanyDelete, name="company-delete"),
    path('company/<int:company_id>/update', views.CompanyUpdate, name="company-update"),
    path('company/entry', views.CompanyEntry, name="company-entry"),
]
