from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import get_template
from .forms import ContactForm


def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)
        phone_number = request.POST.get('phone_number', '')
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            phone_number = request.POST.get('phone_number', '')
            message = request.POST.get('message', '')

            # Email the user with their contact information
            template = get_template('reply_template.txt')
            context = {
                'contact_name': contact_name,
                'phone_number': phone_number,
                'message': message,
            }
            content = template.render(context)

            print(context)
            messages.success(request, 'Thanks for getting in touch with us, We will get back to you as soon as possible.')
            return redirect('shop:index')

        else:
            print(form.errors)

    return render(request, "contact.html", {'form': form})