from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CompanyForm
from .models import Company


def index(request):
    context = {}
    return render(request, 'broker/index.html', context)


def CompanyList(request):
    companies = Company.objects.all()
    return render(request, 'broker/company/list.html', {'list': companies})

def CompanyDelete(request):
    print(request)

def CompanyEntry(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name)
            print(email)
            c = Company(name=name, email=email)
            c.save()
            return HttpResponseRedirect('/')
    else:
        form = CompanyForm()

    return render(request, 'broker/company/entry.html', {'form': form})
