from django.shortcuts import render
from django.views import generic
from django.conf import settings  
import stripe
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Category,Tool,Employee,Designation,BorrowTool
from .forms import CategoryForm,ToolForm,EmployeeForm,DesignationForm,BorrowToolForm
from django.views import View
from django.core.mail import send_mail
from .resources import BorrowToolResource
from django.db.models import Q
# from techbox.settings import MAIL
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from .tasks import *
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings # new


####################################################################################################################

# class HomePageView(TemplateView):
#     template_name = 'dashboard/test.html'

class ChargeView(TemplateView):
    template_name = 'dashboard/charge.html'



# class SuccessView(TemplateView):
#     template_name = 'dashboard/success.html'


# class CancelledView(TemplateView):
#     template_name = 'dashboard/cancelled.html'


# # new
# @csrf_exempt
# def stripe_config(request):
#     if request.method == 'GET':
#         stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
#         return JsonResponse(stripe_config, safe=False)


# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'GET':
#         domain_url = 'http://localhost:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:

#             checkout_session = stripe.checkout.Session.create(
#                 success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=domain_url + 'cancelled/',
#                 payment_method_types=['card'],
#                 mode='payment',
#                 line_items=[
#                     {
#                         'name': 'T-shirt',
#                         'quantity': 1,
#                         'currency': 'inr',
#                         'amount': '25000',
#                     }
#                 ]
#             )
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})



stripe.api_key = settings.STRIPE_SECRET_KEY # new


class HomePageView(TemplateView):
    template_name = 'dashboard/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'dashboard/charge.html')


# def charge(request):
#     if request.method == 'POST':
#         # import pdb; pdb.set_trace()
#         amount = int(request.POST['amount'])
#         name = request.POST['uname']
#         email = request.POST['email']
#         customer = stripe.Customer.create(
#             email=email,
#             name=name,
#             source=request.POST['stripeToken'],
#             )
#         charge = stripe.Charge.create(
#             customer=customer,
#             amount=amount*100,
#             currency='inr',
#             description="pay amount"
#         )
#         return redirect(reverse('success'))


############################################################################################################


class IndexView(ListView):
    template_name = "index.html"
    queryset=BorrowTool.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_tool_expired'] = self.queryset.filter(expire_on__lte=datetime.now().date(),).count()
        context['tool_expired'] = self.queryset.filter(expire_on__lte=datetime.now().date())
        return context





####################################################################################################################



@method_decorator(login_required, name='dispatch')
class CreateCategoryView(SuccessMessageMixin,CreateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/create_category.html"
    success_url ="/view/category/"
    success_message = "Category was Created successfully"


@method_decorator(login_required, name='dispatch')
#@cache_page(20)
class CategoryView(ListView):
    model = Category
    template_name="dashboard/category_list.html"
    paginate_by = 3
    queryset = Category.objects.all()
    
    


@method_decorator(login_required, name='dispatch')
class UpdateCategoryView(SuccessMessageMixin,UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/update_category.html"
    success_url = "/view/category/"
    success_message = "Category was Update successfully"



@login_required
def detail_category(request, id):  
    category = Category.objects.get(id=id) 
    return render(request,'dashboard/category_detailview.html', {'category':category}) 



@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(SuccessMessageMixin,DeleteView):
    model = Category
    success_url = "/view/category/"
    success_message = "Category was Delete successfully"
    
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)



####################################################################################################################


@method_decorator(login_required, name='dispatch')
class CreateToolView(SuccessMessageMixin,CreateView):
    form_class = ToolForm
    model = Tool
    template_name = "dashboard/tool.html"
    success_url ="/view/tool/"
    success_message = "Tool was Created successfully"





@method_decorator(login_required, name='dispatch')
class ToolView(ListView):
    model = Tool
    template_name="dashboard/tool_list.html"
    paginate_by = 3
    queryset = Tool.objects.all()    



@method_decorator(login_required, name='dispatch')
class UpdateToolView(SuccessMessageMixin,UpdateView):
    form_class = ToolForm
    model = Tool
    template_name = "dashboard/update_tool.html"
    success_url = "/view/tool/"
    success_message = "Tool was Update successfully"
    



@login_required
def detail_tool(request, id):  
    tool = Tool.objects.get(id=id) 
    return render(request,'dashboard/tool_detailview.html', {'tool':tool}) 



@method_decorator(login_required, name='dispatch')
class ToolDeleteView(SuccessMessageMixin,DeleteView):
    model = Tool
    success_url = "/view/tool/"
    success_message = "Tool was Delete successfully"
    
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)




class SearchToolView(ListView):
    model = Tool
    template_name = 'dashboard/search_tool.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # new
        object_list = Tool.objects.filter(
            Q(name__icontains=query) | Q(model_number__icontains=query)
        )
        return object_list



#########################################################################################################################

@method_decorator(login_required, name='dispatch')
class CreateEmployeeView(SuccessMessageMixin,CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/create_employee.html"
    success_url ="/view/employee/"
    success_message = "Employee was Created successfully"





@method_decorator(login_required, name='dispatch')
class EmployeeView(ListView):
    model = Employee
    template_name="dashboard/employee_list.html"
    paginate_by = 3
    queryset = Employee.objects.all()    



@method_decorator(login_required, name='dispatch')
class UpdateEmployeeView(SuccessMessageMixin,UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/update_employee.html"
    success_url = "/view/employee/"
    success_message = "Employee was Update successfully"
    



@login_required
def detail_employee(request, id):  
    emp = Employee.objects.get(id=id) 
    return render(request,'dashboard/employee_detailview.html', {'emp':emp}) 



@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(SuccessMessageMixin,DeleteView):
    model = Employee
    success_url = "/view/employee/"
    success_message = "Employee was Delete successfully"

    
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)


#########################################################################################################################


@method_decorator(login_required, name='dispatch')
class CreateDesignationView(SuccessMessageMixin,CreateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/create_designation.html"
    success_url ="/view/designation/"
    success_message = "Designation was Created successfully"





@method_decorator(login_required, name='dispatch')
class DesignationView(ListView):
    model = Designation
    template_name="dashboard/designation_list.html"
    paginate_by = 3
    queryset = Designation.objects.all()    



@method_decorator(login_required, name='dispatch')
class UpdateDesignationView(SuccessMessageMixin,UpdateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/update_designation.html"
    success_url = "/view/designation/"
    success_message = "Designation was Update successfully"
      




@login_required
def detail_designation(request, id):  
    des = Designation.objects.get(id=id) 
    return render(request,'dashboard/designation_detailview.html', {'des':des}) 



@method_decorator(login_required, name='dispatch')
class DesignationDeleteView(SuccessMessageMixin,DeleteView):
    model = Designation
    success_url = "/view/designation/"
    success_message = "Designation was Delete successfully"

    
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)


#########################################################################################################################


# class BorrowToolView(View):
#     def get(self, request, *args, **kwargs):
#         context = {'form': BorrowToolForm()}
#         return render(request, 'dashboard/borrowtool.html', context)

#     def post(self, request, *args, **kwargs):
#         form = BorrowToolForm(request.POST)
#         if form.is_valid():
#             employee=Employee.objects.all()  
#             for i in employee:
#                 print(i.email)
#             MAIL(i.email)    
#             form.save()

#             return HttpResponseRedirect("/")
#         return render(request, 'dashboard/borrowtool.html', {'form': form})



class BorrowAssignToolView(View):
    def get(self, request, *args, **kwargs):
        form = BorrowToolForm()
        return render(request,'dashboard/borrowtool.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form = BorrowToolForm(request.POST or None)
        if form.is_valid():
            email= form.cleaned_data['employee']
            tool= form.cleaned_data['tool']
            expire= form.cleaned_data['expire_on']
            object=form.save(commit=False)
            employee=Employee.objects.get(email=email)
            name=employee.name
            print(name)
            object.release=True
            object.save()
            messages.success(self.request,f"{tool} borrowed by {employee.name} Successfully ")
            subject = 'welcome to GFG world'
            message = f'Hi {name}, You have got {tool}. for {expire}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )

        return HttpResponseRedirect("/view/assign/tool")



@method_decorator(login_required, name='dispatch')
class BorrowToolView(ListView):
    model = BorrowTool
    template_name="dashboard/view_assign_tool.html"
    paginate_by = 3
    queryset = BorrowTool.objects.all()    




@login_required
def detail_assigntool(request, id):  
    assign = BorrowTool.objects.get(id=id) 
    return render(request,'dashboard/detail_assigntool.html', {'assign':assign}) 




@method_decorator(login_required, name='dispatch')
class AssignToolDeleteView(SuccessMessageMixin,DeleteView):
    model = BorrowTool
    success_url = "/view/assign/tool"
    success_message = "Borrow Tool was Delete successfully"

    
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)




def export_data(request):
    
    if request.method == 'POST':
        file_format = request.POST['file-format']
        borrowtool_resource = BorrowToolResource()
        queryset = BorrowTool.objects.all()
        dataset = borrowtool_resource.export(queryset)
        
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="borrow_tool_Backup.csv"'
            return response        
        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="borrow_tool_Backup.json"'
            return response

        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="borrow_tool_Backup.xls"'
            return response   
          
    
    return redirect('/dashboard/view/assign/tool')


class ReleaseToolView(View):
    def get(self,request,id):
        query=BorrowTool.objects.filter(id=id).update(release=False)
        queryset=BorrowTool.objects.filter(id=id).update(release_on=timezone.now())
        messages.success(request,"Tool Submitted Successfully")
        return HttpResponseRedirect("/dashboard/view/assign/tool")


################################################################################################################################