from .serializers import ToolSerializers,BorrowToolSerializers,DesignationSerializer,EmployeeSerializer
from .models import Tool,BorrowTool,Designation,Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .import serializers
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # <-- Here


###########################################################################################################################

class EmployeeCreateApi(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


###########################################################################################################################

class EmployeeListApi(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


###########################################################################################################################


class DesignationCreateApi(CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer



###########################################################################################################################

class ToolListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        tools = Tool.objects.all()
        serializer = ToolSerializers(tools, many=True)
        return Response(serializer.data)

    def post(self, request, formar=None):
        serializer = ToolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########################################################################################################################


class ToolDetailApi(APIView):

    def get_object(self, pk):
        try:
            return Tool.objects.get(pk=pk)
        except Tool.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        tool = self.get_object(pk)
        serializer = ToolSerializers(tool)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tool = self.get_object(pk)
        serializer = ToolSerializers(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tool = self.get_object(pk)
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###########################################################################################################################

class BorrowToolApi(APIView):

    def get(self, request):
        borrowlist = BorrowTool.objects.all()
        serializer = BorrowToolSerializers(borrowlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BorrowToolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



###########################################################################################################################


class BorrowToolDetailApi(APIView):

    def get_object(self, pk):
        try:
            return BorrowTool.objects.get(pk=pk)
        except BorrowTool.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        borrowtool = self.get_object(pk)
        serializer = BorrowToolSerializers(borrowtool)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        borrowtool = self.get_object(pk)
        serializer = BorrowToolSerializers(borrowtool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        borrowtool = self.get_object(pk)
        borrowtool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###########################################################################################################################


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


###########################################################################################################################