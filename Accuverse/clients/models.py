from django.db import models

# Create your models here.
class Clientinfo(models.Model):
    company_name=models.CharField(max_length=50)
    client_name=models.CharField(max_length=20)
    phone=models.IntegerField()
    representative_name=models.CharField(null=True,blank=True)
    representative_phone=models.IntegerField(null=True,blank=True)
    VAT_TRN=models.IntegerField(null=True,blank=True)
    Trade_licenceNum=models.IntegerField(null=True,blank=True)
    FTA_email=models.EmailField(null=True,blank=True)
    FTA_password=models.CharField(null=True,blank=True)
    #TAX and CT info
    Tax_return_months=models.CharField(null=True,blank=True)
    Financial_year=models.CharField(null=True,blank=True)

