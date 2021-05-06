from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Tool,BorrowTool,Designation,Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        




class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
       


class ToolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ("__all__")



class BorrowToolSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowTool
        fields = ('id', 'employee' ,'tool', 'assign_on','expire_on')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



