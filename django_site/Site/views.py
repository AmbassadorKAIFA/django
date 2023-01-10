from datetime import (date, datetime)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, UpdateView)

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .forms import (CreateTableDataForm, DateInputTableForm, TableBookingForm, AppointmentForm)
from .models import Table

import smtplib, ssl


class MyPage(ListView):
    model = Table
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    # def get(self, request):
    #     form = DateInputTableForm()
    #     return render(request, "index.html", {"form": form})

EMAIL_HOST = 'smtp.gmail.com'
subject = 'Thank you for registering to our site'
content = 'It means a world to us'

# class Mail:
#     def __init__(self):
#         self.port = 587
#         self.smtp_server_domain_name = "smtp.gmail.com"
#         self.sender_mail = "vladtkach925@gmail.com"
#         self.password = "Lolaca2282003-"
#
#     def send(self, emails, subject, content):
#         ssl_context = ssl.create_default_context()
#         service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context = ssl_context)
#         service.login(self.sender_mail, self.password)
#
#         for email in emails:
#             result = service.sendmail(self.sender_mail, email, f"subject: {subject}\n{content}")
#
#             service.quit()
#
# mail = Mail()
#
# mail.send([''], subject, content)
# def appointment_form(request):
#     form = AppointmentForm()
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             print(form.cleaned_data['email'])
#             print(request.POST.get('url_from'))
#
#         return redirect('/')





class CreateTableDataView(CreateView):
    model = Table
    template_name = 'create_table_data.html'
    form_class = CreateTableDataForm
    success_url = reverse_lazy('index')


class ListTablesView(ListView):
    model = Table
    template_name = 'list_tables.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return self.model.objects.all()


class TableListView1(ListView):
    model = Table
    template_name = 'index.html'
    extra_context = {'date': DateInputTableForm}

    def get_queryset(self):
        if self.request.GET.get('date'):
            return self.model.objects.filter(
                date=self.request.GET['date'],
                # booking=False
            )
        return self.model.objects.filter(booking=False)


class TableBookingView(UpdateView):
    model = Table
    template_name = 'booking_table.html'
    form_class = TableBookingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        table = form.save(commit=False)
        table.booking = True
        return super().form_valid(form=form)