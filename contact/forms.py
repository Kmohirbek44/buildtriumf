from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full name *', widget=forms.TextInput({'placeholder': 'Enter your full name'}), required=True)
    phone_number = PhoneNumberField(region='UZ',error_messages={'invalid': 'Telefon raqamingizni 998247312 asnosida kiriting'},
                   widget=forms.TextInput({'placeholder': 'Enter your number'}), required=False)
    message = forms.CharField(label='Your enquiry *', widget=forms.Textarea({'placeholder': 'Enter your message'}), required=True)