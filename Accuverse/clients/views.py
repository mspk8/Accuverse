from django.shortcuts import render,HttpResponse
from .models import*
from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Clientinfo, Service
from calendar import month_name



# Create your views here.

def clients_main(request):
    clients = Clientinfo.objects.all()
    return render(request,"clients_main.html",{"show_clients":clients})

def manage(request):
    clients = Clientinfo.objects.all()
    return render(request,"clients_manage.html",{"show_clients":clients})

@csrf_protect
def client_add(request):
    months = list(enumerate(month_name))[1:]
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        representative_name = request.POST.get('representative_name')
        representative_phone = request.POST.get('representative_phone')
        VAT_TRN = request.POST.get('VAT_TRN')
        onboarding_date = request.POST.get('onboarding_date')
        notes = request.POST.get('notes')
        services = request.POST.getlist('services')  # Multiple selected services
        financial_year=request.POST.get('financial_year')
        vat_return_months=request.POST.getlist('vat_return_months')
        ct_financial_year=request.POST.get("ct_financial_year")
        FTA_email=request.POST.get('FTA_email')
        FTA_password=request.POST.get('FTA_email')
        # Create Clientinfo instance (without services yet)
        client = Clientinfo.objects.create(
            company_name=company_name,
            client_name=client_name,
            client_email=client_email,
            phone=phone,
            address=address,
            representative_name=representative_name,
            representative_phone=representative_phone,
            VAT_TRN=VAT_TRN,
            onboarding_date=onboarding_date,
            next_VAT_return=None,
            next_CT_return=None,
            notes=notes,
            financial_year=financial_year,
            vat_return_months=vat_return_months,
            ct_financial_year=ct_financial_year,
            FTA_email=FTA_email,
            FTA_password=FTA_password
            # Add notes field if present in model; you don't have 'notes' field in your model — add it if you want
        )
        # Save notes if you want, add 'notes' field to model.

        # Add ManyToMany related services
        # First get Service instances by names (assuming service names match exactly)
        services_qs = Service.objects.filter(name__in=services)
        client.services.set(services_qs)

        # Save client with services
        client.save()

        return redirect('add-clients')  # Make sure url name matches your urls.py

    return render(request, 'clients_manage_add.html')


def client_details(request,pk):
     client = get_object_or_404(Clientinfo, pk=pk)
     return render(request, 'clients_details.html', {'client': client})

