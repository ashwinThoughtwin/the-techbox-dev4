from account import views
from django.urls import path, include
from account import urls as account_urls
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

#########################################################################################################################################

urlpatterns = [
	
	path('login/',views.loginuser,name='login'),
	path('signup/',views.SignupView.as_view(),name='signup'),
	path('check/user/',views.CheckuserView.as_view(),name='check/user/'),
	path('logout/',views.logoutView.as_view(),name="logout"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
	path("change/password/",views.ChangePasswordView.as_view(),name="change/password"),
    

#########################################################################################################################################

    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/commons/password-reset/password_reset.html',
             subject_template_name='account/commons/password-reset/password_reset_subject.txt',
             email_template_name='account/commons/password-reset/password_reset_email.html',
             success_url='/account/user_login'
         ),
         name='password_reset'),
    

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]


#########################################################################################################################################