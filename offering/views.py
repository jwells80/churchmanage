from django.shortcuts import render, redirect
from .models import offering, fund, paymenttype
from django.contrib.auth.decorators import login_required
from .forms import paymenttypeForm, fundForm

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'offering/home.html', {
            'title': 'Dashboard',
        })
    else:
        return redirect('accounts/login')

def offeringlist(request):
    gifts = offering.objects.all()
    return render(request, 'offering/offeringlist.html', {'title': 'Offering', 'gifts': gifts})

def funds(request):
    funds = fund.objects.all()
    return render(request, 'offering/funds.html', {'title': 'Funds', 'funds': funds})

def payment(request):
    paytypes = paymenttype.objects.all()
    return render(request, 'offering/paytype.html', {'title': 'Payment Types', 'paytypes': paytypes})

def addpaytype(request):
    if request.method == 'POST':
        form = paymenttypeForm(request.POST)
        if form.is_valid():
            return redirect('offering/mode')
    else:
        form = paymenttypeForm()
    return render(request, 'offering/addpaytype.html', {'title': 'Add Pay Type', 'form': form})

def addfund(request):
    if request.method == 'POST':
        form = fundForm(request.POST)
        if form.is_valid():
            return redirect('offering/mode')
    else:
        form = fundForm()
    return render(request, 'offering/addfund.html', {'title': 'Add Fund', 'form': form})