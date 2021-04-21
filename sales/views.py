from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sales, Agent, FirmUser
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import datetime
import csv
from .forms import FirmUserForm


from django.template.loader import render_to_string

import tempfile
from django.db.models import Sum
# Create your views here.

def accindex(request):
    accdetails = FirmUser.objects.all()
    paginator = Paginator(accdetails, 4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'accdetails': accdetails,
        'values': request.POST
    }
    return render(request, 'profile.html', context)


def accountSettings(request):
    accdetails = FirmUser.objects.all()
    context = {
        'accdetails': accdetails,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'add-profile.html', context)

    if request.method == 'POST':
        firmname = request.POST['firmname']
        gstin = request.POST['gstin']

        if not firmname:
            messages.error(request, 'Firm name is required')
            return render(request, 'add-profile.html', context)
        if not gstin:
            messages.error(request, 'GSTIN is required')
            return render(request, 'add-profile.html', context)
        
        FirmUser.objects.create(firmname=firmname, gstin=gstin)
        messages.success(request, 'Firm Name Saved Successfully')

        return redirect('profile')

def EditAcc(request):
    accdetails = FirmUser.objects.all()
    context = {
        'accdetails': accdetails,
        'values': request.POST
    }


    if request.method == 'GET':
        return render(request, 'edit-profile.html')

    if request.method == 'POST':
        firmname = request.POST['firmname']
        gstin = request.POST['gstin']

        if not firmname:
            messages.error(request, 'Firm name is required')
            return render(request, 'profile.html', context)

        if not gstin:
            messages.error(request, 'GSTIN is required')
            return render(request, 'profile.html', context)

    accdetails.owner=request.user
    accdetails.firmname = firmname
    accdetails.gstin = gstin
    accdetails.update()
    messages.success(request, 'Business Info updated Successfully')

    return redirect('profile')
    

    
        


    

    




def sales(request):
    current_user = request.user
    agents = Agent.objects.all()
    sales = Sales.objects.filter(owner=request.user)
    paginator = Paginator(sales, 6)
    page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'sales':sales,
        # 'page_obj': page_obj,
    }
    return render(request, 'sales.html', context)

def add_sale(request):
    current_user = request.user

    agents = Agent.objects.all()
    context = {
        'agents' : agents,
        'values' : request.POST,
    }

    if request.method=='GET':
        return render(request, 'add_sale.html', context)
    
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.warning(request, 'Amount is required')
            return render(request, 'add_sale.html', context)
        
        billno = request.POST.get('billno', False)
        if not billno:
            messages.warning(request, 'Invoice Number is required')
            return render(request, 'add_sale.html', context)


        compname = request.POST.get('compname', False)
        if not compname:
            messages.warning(request, 'Company Name is required')
            return render(request, 'add_sale.html', context)

        vehicleno = request.POST.get('vehicleno', False)
        if not vehicleno:
            messages.warning(request, 'Vehicle Number is required')
            return render(request, 'add_sale.html', context)

        quantity = request.POST.get('quantity', False)
        if not quantity:
            messages.warning(request, 'Quantity is required')
            return render(request, 'add_sale.html', context)

        date = request.POST.get('date', False)
        if not date:
            messages.warning(request, 'Date is required')
            return render(request, 'add_sale.html', context)

        rate = request.POST.get('rate', False)
        if not rate:
            messages.warning(request, 'Rate is required')
            return render(request, 'add_sale.html', context)

        hsn = request.POST.get('hsn', False)
        if not hsn:
            messages.warning(request, 'HSN Code is required')
            return render(request, 'add_sale.html', context)

        description = request.POST.get('description', False)
        if not description:
            messages.warning(request, 'Description is required')
            return render(request, 'add_sale.html', context)

        pan = request.POST.get('pan', False)
        if not pan:
            messages.warning(request, 'PAN Number is required')
            return render(request, 'add_sale.html', context)

        agent = request.POST.get('agent', False)
        if not agent:
            messages.warning(request, 'PAN Number is required')
            return render(request, 'add_sale.html', context)

               

        Sales.objects.create(
            owner=request.user, 
            amount=amount, 
            date=date, 
            description=description, 
            agent=agent,
            billno= billno,
            pan=pan,
            hsn=hsn,
            compname=compname,
            rate=rate,
            quantity=quantity,
            vehicleno=vehicleno,)
        messages.success(request, 'Sales Bill Saved Successfully')

        return redirect('sales')

        

