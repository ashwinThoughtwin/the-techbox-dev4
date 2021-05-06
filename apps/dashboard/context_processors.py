
import os
import django
from account.models import Registration
from dashboard.models import Tool,Employee,BorrowTool
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from datetime import date 

###################################################################################################################################################################



# def profile_pic(request):
#     if request.user:
#         if request.user.registration.profile_pic:
#             return {'profile_pic': request.user.registration.profile_pic.url}
#     return {'profile_pic':'/static/assets/img/theme/team-4.jpg'}


def profile_pic(request):
 
    if(request.user.id):

        context = {}
        data = Registration.objects.get(user__id=request.user.id)
        context["data"] = data

        tools = Tool.objects.all().count()

        return {
        
        'data':data,
        
        }

    return {}

###################################################################################################################################################################

def counter(request):
    if (request.user.id):
        tools = Tool.objects.all().count()
        emps = Employee.objects.all().count()
        borrowtool = BorrowTool.objects.all().count()
        tech_tool_expired = BorrowTool.objects.filter(expire_on__lte=datetime.now().date()).count()
        tool_expired = BorrowTool.objects.filter(expire_on__lte=datetime.now().date())
        print(tools)

        return{

		'tools':tools,
        'emps':emps,
        'borrowtool':borrowtool,
        'tech_tool_expired':tech_tool_expired,
        'tool_expired':tool_expired


		}
    return{}

###################################################################################################################################################################



# def expire_tool(request):
#     if (request.user.id):
#         dues_tool= BorrowTool.objects.all(renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)])
#         ex_tool = dues_tool.count()
#         print(dues_tool)

#         return{

#         'dues_tool':dues_tool,
#         'ex_tool':ex_tool

#         }
#     return{}
