from django.db import models
from datetime import datetime
# Create your models here.

class Tenant(models.Model):
  tenant_name = models.CharField(max_length=50)
  tenant_lastName = models.CharField(max_length=50)
  tenant_phoneN = models.CharField(max_length=10)
  tenant_mail = models.CharField(max_length=100)
  tenant_revenue = models.IntegerField()

  def __str__(self):
      return "%s %s" % (self.tenant_name, self.tenant_lastName)

class Owner(models.Model):
  owner_name = models.CharField(max_length=50)
  owner_lastName = models.CharField(max_length=50)
  owner_phoneN = models.CharField(max_length=10)
  owner_email = models.EmailField(max_length=100)
  owner_revenue = models.IntegerField()
  owner_asset = None

  def __str__(self):
      return "%s %s" % (self.owner_name, self.owner_lastName)

class Asset(models.Model):
  asset_tenant = models.ForeignKey(Tenant, default = 1, verbose_name="Tenant", on_delete=models.CASCADE)
  asset_owner = models.ForeignKey(Owner, default = 1, verbose_name="Owner", on_delete=models.SET_DEFAULT)
  asset_value = models.IntegerField()
  asset_city = models.CharField(max_length = 20)
  asset_startDate = models.DateTimeField("Start Date", default=datetime.now())
  asset_endDate = models.DateTimeField("End Date", default=datetime.now())
  asset_adress = models.CharField(max_length = 200, default=1)

  def __str__(self):
      return self.asset_adress