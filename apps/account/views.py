from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth 
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from .models import Registration
from django.core.mail import EmailMessage
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#########################################################################################################################################        


class SignupView(View):

	def post(self,request):
		if "user_id"in request.COOKIES:
			uid = request.COOKIES["user_id"]
			usr = get_object_or_404(User,id=uid)
			login(request,usr)
			if usr.is_superuser:
				return HttpResponseRedirect("/admin")
			if usr.is_active:
				return HttpResponseRedirect("/dashboard")
		if request.method=="POST":
			fname = request.POST["first"]
			last = request.POST["last"]
			un = request.POST["uname"]
			pwd = request.POST["password"]
			em = request.POST["email"]
			con = request.POST["contact"]
			
			usr = User.objects.create_user(un,em,pwd)
			usr.first_name = fname
			usr.last_name = last
			
			usr.save()

			reg = Registration(user=usr, contact_number=con)
			reg.save()
			return render(request,"account/signup.html",{"status":"Mr/Miss. {} your Account created Successfully".format(fname)})
		return render(request,"account/signup.html")


	def get(self,request):
		return render(request,'account/signup.html')	


#########################################################################################################################################        


class CheckuserView(View):
	def get(self,request):
		if request.method=="GET":
			un = request.GET["usern"]
			check = User.objects.filter(username=un)
			if len(check) == 1:
				return HttpResponse("Exists")
			else:
				return HttpResponse("Not Exists")



    
#########################################################################################################################################        


def loginuser(request):
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["password"]

        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                messages.success(request," Successfully Logged in ")
                res = HttpResponseRedirect("/dashboard")
                if "rememberme" in request.POST:
                    res.set_cookie("user_id",user.id)
                    res.set_cookie("date_login",datetime.now())
                return res
        else:
            messages.success(request,"Incorrect username or Password")
            return render(request,"account/login.html")

    #return render(request,"account/login.html")
    if request.user.is_authenticated:
        return redirect('/dashboard')

    else:
        return render(request,'account/login.html')    
    

#########################################################################################################################################



class ProfileView(View):
    def post(self,request):
        context = {}
        check = Registration.objects.filter(user__id=request.user.id)

        if len(check)>0:
            data = Registration.objects.get(user__id=request.user.id)
            print(data)
            context["data"]=data

        if request.method=="POST":
            fn = request.POST["fname"]
            ln = request.POST["lname"]
            em = request.POST["email"]
            con = request.POST["contact"]
            age = request.POST["age"]
            ct = request.POST["city"]
            gen = request.POST["gender"]
            occ = request.POST["occ"]
            abt = request.POST["about"]

            usr = User.objects.get(id=request.user.id)
            usr.first_name = fn
            usr.last_name = ln
            usr.email = em
            usr.save()

            data.contact_number = con
            data.age = age
            data.city = ct
            data.gender = gen
            data.occupation = occ
            data.about = abt
            data.save()


            if "image" in request.FILES:
                img = request.FILES["image"]
                data.profile_pic = img
                data.save()


            context["status"] = ""
            messages.success(request, ' Successfully Update Profile ')
        return render(request,"account/profile.html",context)


    def get(self,request):
        return render(request,'account/profile.html')	

	

#########################################################################################################################################

class ChangePasswordView(View):
    def post(self,request):
        context={}
        ch = Registration.objects.filter(user__id=request.user.id)
        
        if len(ch)>0:
            data = Registration.objects.get(user__id=request.user.id)
            context["data"] = data
        
        if request.method=="POST":
            current = request.POST["cpwd"]
            new_pas = request.POST["npwd"]

            user = User.objects.get(id=request.user.id)
            un = user.username
            check = user.check_password(current)

            if check==True:
                user.set_password(new_pas)
                user.save()
                messages.success(request," Password Changed Successfully!!! ")
                context["msz"] = "Password Changed Successfully!!!"
                context["col"] = "alert-success"
                user = User.objects.get(username=un)
                login(request,user)

            else:
                messages.success(request," Incorrect Current Password!!! ")
                context["msz"] = "Incorrect Current Password"
                context["col"] = "alert-danger"

        return render(request,"account/change_password.html",context)


    def get(self,request):
        return render(request,'account/change_password.html')   



#################################################################################################################


@method_decorator(login_required, name='dispatch')
class logoutView(View):
    def get(self,request):
        logout(request)
        res =  HttpResponseRedirect("/")
        res.delete_cookie("user_id")
        res.delete_cookie("date_login")
        messages.success(request,"Successfull Logged Out")
        return res


#########################################################################################################################################
