from django.test import TestCase,Client
from  .api_views import ToolListApi,BorrowToolApi,Employee
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json
from .models import Tool,BorrowTool



class ViewEmployeeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.designation_data={'id':1,'name':'ROR'}
        self.employee_data = {"id":1,"name": "ishwar mandloi","email": "ishwarmandloi25@gmail.com", "designation": 1,"phone": "8827277049","address": "indore "}
        self.response = self.client.post(
            reverse('api_designation_create'),
            self.designation_data,
            format="json")
        self.response = self.client.post(
            reverse('api_employee_create'),
            self.employee_data,
            format="json")

    def test_01_api_employeelist(self):
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    # def test_02_api_can_get_a_employeelist(self):
    #     employeelist = Employee.objects.last()
    #     response = self.client.get(reverse('api_employee_list'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, employeelist)    



# class ViewItemTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.catagory_data={'id':1,'name':'electronics_gadgets'}
#         self.item_data = {"id":1,"name": "pendrive", "model_no":"m1", "status":True, "catagory": 1}
#         self.response = self.client.post(
#             reverse('api_catagory_create'),
#             self.catagory_data,
#             format="json")
#         self.response = self.client.post(
#             reverse('api_item_create'),
#             self.item_data,
#             format="json")

#     def test_02_api_can_create_a_itemlist(self):
#         response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)