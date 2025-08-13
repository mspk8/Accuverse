from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class finyear(models.Model):
      year = models.CharField(max_length=100, unique=True)
      def __str__(self):
        return self.year
    

class Clientinfo(models.Model):
    company_name = models.CharField(max_length=50)
    client_name = models.CharField(max_length=20)
    client_email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)  # Use CharField for phones (can include + etc.)
    address = models.CharField(max_length=255, null=True, blank=True)
    representative_name = models.CharField(max_length=50, null=True, blank=True)
    representative_phone = models.CharField(max_length=20, null=True, blank=True)
    VAT_TRN = models.CharField(max_length=50, null=True, blank=True)
    FTA_email = models.EmailField(null=True, blank=True)
    FTA_password = models.CharField(max_length=100, null=True, blank=True)
    onboarding_date = models.DateField(null=True, blank=True)
    vat_return_months = models.CharField(max_length=100, null=True, blank=True)
    services = models.ManyToManyField(Service, related_name='clients', blank=True)  
    staff_assigned=models.ManyToManyField(User,related_name='assigned_clients',blank=True)
    next_VAT_return= models.DateField(null=True, blank=True)
    next_CT_return=models.DateField(null=True, blank=True)
    financial_year=models.CharField(null=True,blank=True)
    ct_financial_year=models.CharField(null=True,blank=True)
    notes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.company_name
