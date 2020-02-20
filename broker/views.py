from django.views import generic
from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company


def index(request):
    context = {}
    return render(request, 'broker/search/index.html', context)


def CompanyList(request):
    companies = Company.objects.all()
    return render(request, 'broker/company/list.html', {'list': companies})


def CompanyDelete(request, company_id):
    print(request.method)
    if request.method == 'POST':
        print(request)
    context = {}
    return redirect('/company')


def CompanyUpdate(request, company_id):
    context = {}
    print(request)
    return render(request, '/company', context)


def CompanyEntry(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            c = Company(name=name, email=email)
            c.save()
            return redirect('/company')
    else:
        form = CompanyForm()

    return render(request, 'broker/company/entry.html', {'form': form})
