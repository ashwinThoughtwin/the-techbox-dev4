from dashboard import views
from django.urls import path, include
from dashboard import urls as dashboard_urls
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from dashboard.views import export_data
from dashboard import api_views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.decorators.cache import cache_page

#########################################################################################################################################


urlpatterns = [
	
	path('dashboard/',views.IndexView.as_view(),name='index'),
	
	# path('test/',views.HomePageView.as_view(), name='test'),
	# path('config/', views.stripe_config),  # new
	# path('create-checkout-session/', views.create_checkout_session), # new
	# path('success/', views.SuccessView.as_view()), # new
 	#path('cancelled/', views.CancelledView.as_view()), # new
	path('charge/', views.charge, name='charge'), # new
    path('test/', views.HomePageView.as_view(), name='test'),  

					# ------------**--------------#
	
	path('category/',views.CreateCategoryView.as_view(),name='category'),
	path('view/category/',views.CategoryView.as_view(), name='view/category'),
	#path('view/category/',cache_page(20)(views.CategoryView.as_view()), name='view/category'),
	path('update/category/<int:pk>',views.UpdateCategoryView.as_view(),name='update/category'),
	path('detail/category/<int:id>', views.detail_category,name='detail/category'),
	path('delete/category/<int:pk>',views.CategoryDeleteView.as_view(),name='delete/category'),

					# ------------**--------------#

	path('create/tool/',views.CreateToolView.as_view(),name='create/tool'),
	path('view/tool/', views.ToolView.as_view(), name='view/tool'),
	path('update/tool/<int:pk>',views.UpdateToolView.as_view(),name='update/tool'),
	path('detail/tool/<int:id>', views.detail_tool,name='detail/tool'),
	path('delete/tool/<int:pk>',views.ToolDeleteView.as_view(),name='delete/tool'),
	path('search/tool/',views.SearchToolView.as_view(),name='search/tool/'),


					# ------------**--------------#


	path('create/employee/',views.CreateEmployeeView.as_view(),name='create/employee'),
	path('view/employee/', views.EmployeeView.as_view(), name='view/employee'),
	path('update/employee/<int:pk>',views.UpdateEmployeeView.as_view(),name='update/employee'),
	path('detail/employee/<int:id>', views.detail_employee,name='detail/employee'),
	path('delete/employee/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete/employee'),



					# ------------**--------------#


	path('create/designation/',views.CreateDesignationView.as_view(),name='create/designation'),
	path('view/designation/', views.DesignationView.as_view(), name='view/designation'),
	path('update/designation/<int:pk>',views.UpdateDesignationView.as_view(),name='update/designation'),
	path('detail/designation/<int:id>', views.detail_designation,name='detail/designation'),
	path('delete/designation/<int:pk>',views.DesignationDeleteView.as_view(),name='delete/designation'),


					# ------------**--------------#


	path('borrow/tool/',views.BorrowAssignToolView.as_view(),name='borrow/tool'),
	path('view/assign/tool',views.BorrowToolView.as_view(),name='view/assign/tool'),
	path('delete/assign/tool/<int:pk>',views.AssignToolDeleteView.as_view(),name='delete/assign/tool'),
	path('detail/assign/tool/<int:id>', views.detail_assigntool,name='detail/assign/tool'),
	path('release/tool/<int:id>',views.ReleaseToolView.as_view(),name='release/tool'),


					# ------------**--------------#
							# export urls #

	path('export/borrow/tool', export_data, name="export/borrow/tool"),

					# ------------**--------------#
							# api urls #

	 
    path('toollist/api/', api_views.ToolListApi.as_view(), name="toollist/api/"),
    path('tooldetail/api/<int:pk>/', api_views.ToolDetailApi.as_view(), name="tooldetail/api"),
    path('borrow/api/', api_views.BorrowToolApi.as_view(), name="borrow/api"),
    path('borrow/tooldetail/api/<int:pk>/', api_views.BorrowToolDetailApi.as_view(), name="borrow/tooldetail/api"),
    #path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/designation/create',api_views.DesignationCreateApi.as_view(),name='api_designation_create'),
    path('api/employee/create',api_views.EmployeeCreateApi.as_view(),name='api_employee_create'),
    path('api/employee/list',api_views.EmployeeListApi.as_view(),name='api_employee_list'),
]	

