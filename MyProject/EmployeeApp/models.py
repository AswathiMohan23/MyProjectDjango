import uuid
from django.db import models

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=30,verbose_name="company_name",blank=True)
    company_location = models.CharField(max_length=30,verbose_name="company_location",blank=True)


    def __str__(self):
        return str(self.company_name)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'



class Employee(models.Model):
    company = models.ForeignKey(Company, null=True,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name=models.CharField(max_length=200,verbose_name="employee_name",blank=True)
    place = models.CharField(max_length=200,verbose_name="place",blank=True)

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

