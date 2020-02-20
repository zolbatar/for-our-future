from django.views import generic
from django.shortcuts import render, redirect
from .forms import ItemForm, CompanyForm
from .models import Item, Company


def ItemList(request):
    items = Item.objects.all()
    return render(request, 'broker/item/list.html', {'items': items})


def ItemEntry(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            units = form.cleaned_data['units']
            i = Item(company=company, title=title, description=description,
                     price=price, units=units)
            i.save()
            return redirect('/')
    else:
        form = ItemForm()
    companies = Company.objects.all()
    return render(request, 'broker/item/entry.html', {'form': form, 'companies': companies})


def CompanyList(request):
    companies = Company.objects.all()
    return render(request, 'broker/company/list.html', {'companies': companies})


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
