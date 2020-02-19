from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CompanyForm


def index(request):
    context = {}
    return render(request, 'broker/index.html', context)


def get_company(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyForm()

    return render(request, 'broker/company.html', {'form': form})
