import json
from os import access


# from django.views.generic.edit import FormView
from django.contrib import messages
# #from authentication app
# #from app
# from website.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group
from django.core import exceptions
from django.db.models import Q
from django.db.models.aggregates import Avg
# from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
# from django.views.generic import TemplateView
from django.views import View, generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import *
# #functions
from .functions import *
# #models
from core.models import *

# from django.shortcuts import render, get_object_or_404, redirect
# from django.template import loader
# from django.http import HttpResponse
# from django import template

# from django.core.mail import send_mail
# # Create your views here.
from accounts.models import User



def search(request):
    if request.is_ajax():
        query = request.GET.get('query')
        obj = Branch.objects.filter(Q(branch_name__icontains = query) | Q(user__phone__icontains = query))
        data = list()
        for branch in obj:
            data.append({
               'phone': branch.user.phone,
               'branch_name': branch.branch_name,
               'Mobile_No': branch.Mobile_No,
               'city': branch.city,
               'state': branch.state,
               'EmailID': branch.EmailID,
            })
        data = json.dumps(data)
        print(data)
        return JsonResponse({'rv':query, 'obj':data})

    
        
            
        
        
def login_view(request):
    print('......POST')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        db_user = User.objects.get(email = email)
        user = check_password(password,db_user.password)
        if user:
            login(request,db_user)
            messages.success(request,'login successfully')
            return redirect('dashboard:AdminHome')
        else:
            messages.error(request,'given credentials not correct')
            return redirect('index')  
    return render(request, "dashboard/accounts/auth-login.html")
            
        
        
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('dashboard:login')      
             
          



@login_required(login_url="/sbtadmin/login/") 
def index(request):
    # branch_user = PersonalDetails.objects.filter(user=request.user).first()
    # customers = Customer.objects.all()
   
    # c_count =  customers.count()

    # vendors = Vendor.objects.all()
    # v_count =  vendors.count()
    
   
    # active_vendors = Vendor.objects.filter(vendor_is_active=True)
    # active_vendor_count = active_vendors.count()

    # active_customers = Customer.objects.filter(customer_is_active=True)
    # active_customer_count = active_customers.count()
    

    # if slug == api_key:
    return render(request, "dashboard/index.html")
    # else:
        # return HttpResponse('not allowed to access')

# class DetailVendorView(DetailView):
#     model = Vendor
#     template_name = 'dashboard/detail-edit/vendor-view.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# # @login_required(login_url="/sbtadmin/login/")
# def profile(request):
#     return render(request, "dashboard/profile.html")

    




class NewVendorView(View):
    def get(self,request):
        form = NewVendorForm()
        return render(request,'dashboard/forms/NewVendorForm.html',{'form':form})


class VendorRequestView(View):
    def get(self,request):
        return render(request,'dashboard/Requests/VendorRequest.html')

# class AllVendorsView(generic.ListView):
#     """
#     Display All Vendors From Database
#     """
#     model = Vendor
#     paginate_by = 10
#     template_name = 'dashboard/ViewsAll/all_vendors.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context






class ContactUsView(View):
    template_name = 'dashboard/forms/contact_us_form.html'
    initial = {'key': 'value'}
    form_class = ContactForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            branch_user_msg = BranchContact()
            branch_user_msg.branch = Branch.objects.filter(user=request.user).first()
            branch_user_msg.email = form.cleaned_data['email']
            branch_user_msg.desc = form.cleaned_data['description']
            branch_user_msg.save()
            url = f"http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=sbtpro&password=123456&sender=SBTPRO&receiver={8683827398}&route=TA&msgtype=1&sms=Branch { branch_user_msg.branch} wants to contact you\n email is {branch_user_msg.email}\n message is {branch_user_msg.desc}"
            response = requests.request("GET",url)
            messages.success(request,'Message sent! Company executive will contact you as soon as possible')
            return redirect('dashboard:AdminHome')
        return render(request, self.template_name, {'form': form})
