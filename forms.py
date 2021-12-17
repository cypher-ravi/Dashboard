# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


BRANCH_TYPE_CHOICES = (
    ("state", "state"),
    ("district", "district"),
    ("tehsil", "tehsil"),
    ("village", "village"),

)

GENDER_CHOICES = (
    ("1", "Please Select"),
    ("2", "Male"),
    ("3", "Female"),
    ("4", "Other"),

)

STATUS_CHOICES = (
    ("1", "Please Select"),
    ("2", "New"),
    ("3", "Verified"),

)

VALID_STATE_CHOICES = (
    ("1", "Please Select"),
    ("2", "Andra Pradesh"),
    ("3", "Arunachal Pradesh"),
    ("4", "Assam"),
    ("5", "Bihar"),
    ("6", "Chhattisgarh"),
    ("7", "Chandigarh"),
    ("8", "Dadar and Nagar Haveli"),
    ("9", "Daman and Diu"),
    ("10", "Delhi"),
    ("11", "Goa"),
    ("12", "Gujarat"),
    ("13", "Haryana"),
    ("14", "Himachal Pradesh"),
    ("15", "Jammu and Kashmir"),
    ("16", "Jharkhand"),
    ("17", "Karnataka"),
    ("18", "Kerala"),
    ("19", "Lakshadeep"),
    ("20", "Madya Pradesh"),
    ("21", "Maharashtra"),
    ("22", "Manipur"),
    ("23", "Meghalaya"),
    ("24", "Mizoram"),
    ("25", "Nagaland"),
    ("26", "Orissa"),
    ("27", "Punjab"),
    ("28", "Pondicherry"),
    ("29", "Rajasthan"),
    ("30", "Sikkim"),
    ("31", "Tamil Nadu"),
    ("32", "Telagana"),
    ("33", "Tripura"),
    ("34", "Uttaranchal"),
    ("35", "Uttar Pradesh"),
    ("36", "West Bengal"),
    ("37", "Andaman and Nicobar Island"),

)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "value"       : "",
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "value"       : "ApS12_ZZs8",                
                "class"       : "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewVendorForm(forms.Form):
    """
    form for New Vendor

    """
    name_of_company = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name Of Company",
                "class" : "form-control",
                "aria-label" : "Companyname",
                "aria-describedby" : "basic-addon1",
                "type" : "text",
                "id" : "input-company-name",
            }
        ))
    vendor_address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1234 Main St",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress",
            }
        ))
    vendor_address_2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Apartment, studio, or floor",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputAddress2",
            }
        ))
    mobile_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-mobile",

            }
        )
    )
    mobile_no_2 = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "MobileNo 2",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-mobile2",

            }
        )
    )
    fax_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Fax Number",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-fax",

            }
        )
    )
    vendor_email_address = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Vendor Email Address",
                "class" : "form-control",
                "type" : "email",
                "id" : "input-email",
            }
        ))
    
    vendor_website_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Website url",
                "class" : "form-control",
                "type" : "url",
                "id" : "input-url",
            }
        )
    )
    vendor_android_app_url = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "placeholder" : "Android App url",
                "class" : "form-control",
                "type" : "url",
                "id" : "input-app-url",
            }
        )
    )

    vendor_contact_person = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Contact Person",
                "class" : "form-control",
                "type" : "text",
                "id" : "contact-person",
            }
        ))
    landline_number = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Landline number",
                "class" : "form-control form-control-alternative",
                "type" : "text",
                "id" : "input-landline-number",

            }
        )
    )
    date_company_was_established = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "placeholder" : "Established date",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-register",

            }
        )
    )
    vendor_is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "id" : "active"
            }
        ),
        required=False)
    
    vendor_city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "karnal",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputCity",
            }
        )) 

    vendor_state = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "type" : "text",
                "id" : "inputState",
                "class" : "form-control form-control-alternative",
            },
        choices=VALID_STATE_CHOICES
        )
        
    )
    vendor_country = CountryField(blank_label='(select country)').formfield(required=False,widget=CountrySelectWidget(attrs={
        'class':'form-control ',
        "id" : "input-country",
        "type" : "text",
    }))
    zip_code = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Postal code",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputZip",

            }
        )
    )
    extra_info = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "A few words about branch...",
                "class" : "form-control form-control-alternative",

            }
        )
    )
    employee_id_reference = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee name / ID",
                "class" : "form-control",
                "type" : "text",
                "id" : "input-employee",
            }
        )
    )
    tin_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Tin No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputTin",

            }
        )
    )
    pan_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Pan No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputPan",

            }
        )
    )
    gst_no = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Gst No.",
                "class" : "form-control",
                "type" : "text",
                "id" : "inputGst",

            }
        )
    )
    


        
class ContactForm(forms.Form):
    """
    form for submittion of branch report

    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Enter Email",
                "class" : "form-control ",
                "type" : "email",
                "id" : "Email",
            }
        ))
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Message",
                "class" : "form-control ",
                "type" : "text",
                "id" : "description",
            }
        ))
    
        
    