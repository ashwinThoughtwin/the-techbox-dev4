from django import forms  
from .models import Category,Tool,Employee,Designation,BorrowTool

##########################################################################################################################


class CategoryForm(forms.ModelForm):  
    
    class Meta:
        model = Category
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Category'}),  
        }
        fields = "__all__"


##########################################################################################################################

class ToolForm(forms.ModelForm):  
    
    class Meta:
        model = Tool
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'category' : forms.Select(attrs={'class':'form-control','placeholder':'Category'}),
            'model_number' : forms.TextInput(attrs={'class':'form-control','placeholder':'Model Number'}),
        	
        }
        fields = "__all__"
        


##########################################################################################################################


class EmployeeForm(forms.ModelForm):  
    
    class Meta:
        model = Employee
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'designation': forms.Select(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'Number','class':'form-control'}), 
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}), 
        }
        fields = "__all__"


##########################################################################################################################


class DesignationForm(forms.ModelForm):  
    
    class Meta:
        model = Designation
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),  
        }
        fields = "__all__"


##########################################################################################################################


class BorrowToolForm(forms.ModelForm):  
    class Meta:
        model = BorrowTool
        widgets = {
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'tool' : forms.Select(attrs={'class':'form-control'}),
            'assign_on' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
            'expire_on' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
       }
        fields = "__all__"