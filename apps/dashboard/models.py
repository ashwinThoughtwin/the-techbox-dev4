from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


######################################################################################################################################

#STATUS=((0,'Deactive'),(1,'Active'))



######################################################################################################################################

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,default="")
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name


######################################################################################################################################

class Tool(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100,null=True,blank=True,default="")
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.name 

######################################################################################################################################


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey('Designation',on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    #status=models.IntegerField(choices=STATUS,default=1)
    status =models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.email

######################################################################################################################################


class Designation(models.Model):
    name = models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


######################################################################################################################################

class BorrowTool(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    tool=models.ForeignKey(Tool,on_delete=models.CASCADE)
    assign_on=models.DateTimeField()
    expire_on = models.DateTimeField()
    release = models.BooleanField(default=True)
    release_on = models.DateTimeField(null=True,blank=True)
    

    def __str__(self):
        return self.employee.name +"-"+ self.tool.name


######################################################################################################################################


